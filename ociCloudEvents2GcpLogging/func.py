import io
import json
import logging
from fdk import response



def googleLoggerCall(logName, logData):
    '''
    Send the data that needs to be logged to the google logging service. In general the data we do want to send is in
    all cases a JSON structure (dict), however, to be sure that in case the function is (mis-)used for another type of
    integration we do check if the variable type of LogData is either a dict or string. Depending on this we will call
    the google logging client in another fashion.
    :param logName:
    :param logData:
    :return:
    '''


    # Instantiates a google logger client and define the log target to use to write the data. The name of the log is
    # defined by the user in the form of a function variable when configuring the function in Oracle Cloud.
    GoogleloggingClient = logging.Client()
    logger = GoogleloggingClient.logger(logName)

    # check for the type of var, we do expect the var to be a dict holding a JSON structure. However, in case it is a
    # string value we do need to use log_text instead of using log_struct. This will make the logic more robust and able
    # to cope with other data types than only JSON structures.
    if type(logData) is str:
        logger.log_text(logData)
    elif type(logData) is dict:
        logger.log_struct(logData)
    else:
        print("cannot determine what type of var this is")



def handler(ctx, data: io.BytesIO = None):
    '''

    :param ctx:
    :param data:
    :return:
    '''
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

    # The Google Logging Client Libraries requires the service account key JSON file to be present on the operating system
    # and need to be referenced as a file path under the operating system var GOOGLE_APPLICATION_CREDENTIALS . This means
    # that it is required to build the JSON file on the fly based upon the information provided in the configuration of the
    # Oracle Cloud function and that we ensure that the path where the file is created is placed in the mentioned OS env var

    # Create a JSON structure for the Google Key File
    googleKeyFileData = {
        "type": keyFileType,
        "project_id": keyFileProjectId,
        "private_key_id": keyFilePrivateKeyId,
        "private_key": keyFilePrivateKey,
        "client_email": keyFileClientEmail,
        "client_id": keyFileClientId,
        "auth_uri": keyFileAuthUri,
        "token_uri": keyFileTokenUri,
        "auth_provider_x509_cert_url": keyFileAuthProvideCert,
        "client_x509_cert_url": keyFileClientCert
    }

    # Create a local file for writing the google key file and write the JSON structure to it.
    try:
        with open(googleKeyFile, 'w') as outfile:
        json.dump(googleKeyFileData, outfile)
    except:
        funcFailure = True
        funcFailureMessage = ('ERROR - Unable to write Google Keyfile to local function storage')



    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )
