import io
import json
import requests
import datetime
import hashlib
import hmac
import base64
from fdk import response


# Build the API signature to be used in calling the Azure API endpoints. The API signature is used in the authentication
# when pushing data to Azure.
def build_signature(customer_id, shared_key, date, content_length, method, content_type, resource):
    x_headers = 'x-ms-date:' + date
    string_to_hash = method + "\n" + str(content_length) + "\n" + content_type + "\n" + x_headers + "\n" + resource
    bytes_to_hash = bytes(string_to_hash, encoding="utf-8")
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode()
    authorization = "SharedKey {}:{}".format(customer_id, encoded_hash)
    return authorization


# handler is the main logic which is called when the functions is invoked by an external source. The handler is the
# standard way of working for Oracle OCI serverless functions.
def handler(ctx, data: io.BytesIO = None):
    funcFailure = False
    funcFailureMessage = ('ERROR - Unknown error')
    funcResponseMessage = ('OK')

    # try to capture the payload message which should contain the CNCF cloud event which is send to the function by
    # Oracle Cloud. In case we do not receive this an error will be raised
    try:
        receivedCloudEvent = json.loads(data.getvalue())
    except (Exception, ValueError) as ex:
        funcFailure = True
        funcFailureMessage = ('ERROR - No OCI cloud event from OCI send into the function')

    # Get all the function K/V configuration into functionConfig. The configuration of the function can be done within
    # Oracle Cloud. Can be done via the UI or in other ways. The configuration is customer / deployment specific. The
    # default values for all variables is "required" for all. The current prime variables used by this function are:
    # custom_log_name, customer_id, shared_key
    functionConfig = dict(ctx.Config())

    # get the value for custom_log_name. the custom_log_name in used as the name for the custom log in Azure sentinel.
    # it is not needed to create the custom log manually in Azure, it will be created the moment the first log record
    # is send to this custom log.
    try:
        azureCustomLogName = functionConfig.get('custom_log_name')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter custom_log_name')

    # get the value for customer_id. the customer_id is used in calling Azure sentinel
    try:
        azureCustomerId = functionConfig.get('customer_id')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter customer_id')

    #  get the value for shared_key. The shared_key is used in calling Azure sentinel
    try:
        azureSharedKey = functionConfig.get('shared_key')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter shared_key')

    # ensure we only start preparing the call to azure and make the actual call in case we did not encounter an error as
    # that would indicate we will (most likely) fail the call to the Azure API.
    if funcFailure:
        print ("DEBUG - unable to continue in building Azure call due to earlier error.")
    else:

        # ensure we turn receivedCloudEvent into a string var named azurePayLoad by leveraging json.dumps When trying to
        # push a dict into requests.post it will fail.
        azurePayLoad = json.dumps(receivedCloudEvent)

        azureApiMethod = 'POST'
        azureApiContentType = 'application/json'
        azureApiResource = '/api/logs'
        rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        content_length = len(azurePayLoad)

        signature = build_signature(azureCustomerId, azureSharedKey, rfc1123date, content_length, azureApiMethod, azureApiContentType, azureApiResource)
        #uri = azureApiUri
        azureApiUri = 'https://' + azureCustomerId + '.ods.opinsights.azure.com' + azureApiResource + '?api-version=2016-04-01'

        headers = {
            'content-type': azureApiContentType,
            'Authorization': signature,
            'Log-Type': azureCustomLogName,
            'x-ms-date': rfc1123date
        }

        # try to call the Azure Sentinel API endpoint and store the result in azureApiResponse. If this fails we fail
        # the entire function.
        try:
            azureApiResponse = requests.post(azureApiUri, data=azurePayLoad, headers=headers)

        # catch all (other) exceptions, prime use-case that "could" be catched is the issue of being unable to resolve the
        # URI due to a DNS lookup failure.
        except requests.exceptions.RequestException as e:
            funcFailure = True
            funcFailureMessage = ("Forward Function Internal error: {}".format(e))
            pass

    # define the right response message to be send to the caller, taking into account the value of funcFailure. This
    # value will be set to True in case a catched error has been encountered
    if funcFailure:
        return response.Response(
            ctx, response_data=json.dumps(
                {"response": "{0}".format(funcFailureMessage)
                 }),
            headers={"Content-Type": "application/json"}
        )
    else:
        return response.Response(
            ctx, response_data=json.dumps(
                {"response": "OK"
                 }),
            headers={"Content-Type": "application/json"}
        )
