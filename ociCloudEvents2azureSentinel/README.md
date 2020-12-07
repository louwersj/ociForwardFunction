# OCI Cloud Events towards MS Azure Sentinel
The ociCloudEvents2azureSentinel integration function is used to integrate Oracle Cloud and Microsft Azure Sentinel by leveraging the Azure HTTP Data Collector API to send log data to Azure Monitor from a REST API client. It has to be noted that, after an event is posted to the Azure API it takes Azure at the moment around two minutes to process data in the background before it is shown in your workspace. 


## Configuration
To be able to configure the integration you will need some information from Azure. For the integration to work the "workspace ID" and the "primary Key" (or secondary key) are needed. Those can be retreived via the "Agent Management" settings in your Log Analytics Workspace in Micrsoft Azure. The below screenshot shows where the information can be retrieved. 

![](../doc/Azure_sentinel_Oracle_Cloud_2.png)
*Aquire Azure details for Oracle Cloud Configuration*

## Viewing OCI events in Azure
When data is send to Azure you can retrieve the data in your Azure workspace. It has to be noted that, after an event is posted to the Azure API it takes Azure at the moment around two minutes to process data in the background before it is shown in your workspace. The data that is provided to Azure will be stored in a custom log named after the value for custom_log_name which you configured in OCI for this function. Azure will append CL after the name configure in custom_log_name. The below example shows a custom log configured as ociEventTest1 as a custom log in your Azure workspace.

![](../doc/Azure_sentinel_Oracle_Cloud_3.png)
*Custom log with Oracle Cloud Events*

Retrieving and viewing OCI Cloud Events from Oracle Cloud in an Azure workspace can be done by creating a query in Azure and/or using any of the native Azure ways of retrieving data stored in a specific workspace. The below screenshot shows a simple retrievale query. The data shown in the screenshot is data based upon the [test data JSON file](../testdata/example_0.json) which is part of this github Repository.

![](../doc/Azure_sentinel_Oracle_Cloud_1.png)
*Query Microsoft Azure for Oracle Cloud Events*


## Additional information
* [Azure HTTP Data Collector API](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/data-collector-api)
