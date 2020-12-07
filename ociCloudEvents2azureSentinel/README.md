# OCI Cloud Events towards MS Azure Sentinel
The ociCloudEvents2azureSentinel integration function is used to integrate Oracle Cloud and Microsft Azure Sentinel by leveraging the Azure HTTP Data Collector API to send log data to Azure Monitor from a REST API client.


## Configuration
To be able to configure the integration you will need some information from Azure. For the integration to work the "workspace ID" and the "primary Key" (or secondary key) are needed. Those can be retreived via the "Agent Management" settings in your Log Analytics Workspace in Micrsoft Azure. The below screenshot shows where the information can be retrieved. 

![](../doc/Azure_sentinel_Oracle_Cloud_2.png)
*Aquire Azure details for Oracle Cloud Configuration*

## Additional information
* [Azure HTTP Data Collector API](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/data-collector-api)
