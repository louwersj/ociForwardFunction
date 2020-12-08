import io
import json
import logging

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    funcFailure = False
    funcFailureMessage = ('ERROR - Unknown error')

    name = "World"
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    # define the full path to the google key file (including the file name)
    googleKeyFile = ("{}/google_key_file.json".format(os.path.dirname(os.path.realpath(__file__))))

    # Get all the function K/V configuration into functionConfig. The configuration of the function can be done within
    # Oracle Cloud. Can be done via the UI or in other ways. The configuration is customer / deployment specific. The
    # default values for all variables is "required" for all. The current prime variables used by this function are:
    # custom_log_name, customer_id, shared_key
    functionConfig = dict(ctx.Config())

    # Try to extract the value for keyfile_type from the function config. If failed we fail the function
    try:
        keyFileType = functionConfig.get('keyfile_type')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_type')

    # Try to extract the value for keyfile_project_id from the function config. If failed we fail the function
    try:
        keyFileProjectId = functionConfig.get('keyfile_project_id')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_project_id')

    # Try to extract the value for keyfile_private_key_id from the function config. If failed we fail the function
    try:
        keyFilePrivateKeyId = functionConfig.get('keyfile_private_key_id')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_private_key_id')

    # Try to extract the value for keyfile_private_key from the function config. If failed we fail the function
    try:
        keyFilePrivateKey = functionConfig.get('keyfile_private_key')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_private_key')

    # Try to extract the value for keyfile_client_email from the function config. If failed we fail the function
    try:
        keyFileClientEmail = functionConfig.get('keyfile_client_email')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_client_email')

    # Try to extract the value for keyfile_client_id from the function config. If failed we fail the function
    try:
        keyFileClientId = functionConfig.get('keyfile_client_id')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_client_id')

    # Try to extract the value for keyfile_auth_uri from the function config. If failed we fail the function
    try:
        keyFileAuthUri = functionConfig.get('keyfile_auth_uri')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_auth_uri')

    # Try to extract the value for keyfile_token_uri from the function config. If failed we fail the function
    try:
        keyFileTokenUri = functionConfig.get('keyfile_token_uri')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_token_uri')

    # Try to extract the value for keyfile_auth_provider_x509_cert_url from the function config. If failed we fail the function
    try:
        keyFileAuthProvideCert = functionConfig.get('keyfile_auth_provider_x509_cert_url')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_auth_provider_x509_cert_url')

    # Try to extract the value for keyfile_client_x509_cert_url from the function config. If failed we fail the function
    try:
        keyFileClientCert = functionConfig.get('keyfile_client_x509_cert_url')
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to get a value for config parameter keyfile_client_x509_cert_url')

    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )
