# OCI Forward Functions - Event and Log integration for Oracle Cloud
![](/doc/OCIForwardFunctions.png)

The OCI Forward Functions Project is a collection of functions used to integrate Oracle Cloud - OCI - with third party solutions. The primary initial use case is (has been) integrating Oracle Cloud logging and CNCF compatible Oracle Cloud Events. For the creation of the integrations OCI functions are used and written primarily in Python to leverage the concept of clud native serverless as much as possible and to ensure an ease of deployment and use for users. 

From both a security, manageability and visibility point of view enterprises do require a single "pane of glass" / system to consolidate all loging and all Cloud Events. In a general enterprise landscape systems can be located in multiple clouds and on-premise, this drives the need to be able to integrate and consolidate data in one single place. Oracle Cloud provides the options to collect data as the central data collector, however, for situations where the enterprise architecture dictates that events and logging need to be put "somewhere else" integration is needed. The collection of functions within the OCI Forward Functions Project provide a jumpstart in realizing this integration. Even though the ociForwardFunction project is a Oracle Cloud centric project it is not in any way or from affiliated with Oracle as a company. The ociForwardFunction project is a fully open source set of integration functions developed under GPL-3.0 License. 

It is expected that the person implementing one or mulitple of the functions provided by the OCI Forward Functions Project has a basic understanding of OCI, OCI events and the target(s) that are intended for this integration.  

## Integrations

### Microsoft Azure Sentinel - OCI Cloud Events  
Sending OCI Cloud Events to Micorsoft Azure Sentinel for inclusion in a Azure Sentinel log workspace. This can be achieved by using the ociCloudEvents2azureSentinel functionalitly. [Documentation](ociCloudEvents2azureSentinel/README.md)

*Tested = Yes, Operational = Yes*

### Microsoft Azure Sentinel - OCI logging 
Sending OCI logging to Micorsoft Azure Sentinel for inclusion in a Azure Sentinel log workspace. This can be achieved by using the ociLogging2azureSentinel functionalitly.

*Tested = No, Operational = No*

## Deployment and configuration
For the full working of functions provided by the OCI Forward Functions Project it is requried that the functions will be deployed and configured and that (for the event and logging functions) the correct configuration is done to ensure that the logging and event information is send to the functions to trigger them and invoke the logic in the functions that will ensure the ingration to a third party system. The below sub-sections provide guidance for this. 

### Generic Function Deployment
The OCI Forward Functions Project consists out of pure OCI functions (based upon Fn Project - the container native serverless framework). Due to this deployment of the functions towards Oracle Cloud will follow the standard deployment model as for any function deployment in OCI. 

To ensure a basic understanding of how to configure / prepare OCI for function deployments please do refer to the following documentation:
* [Creating and Deploying Functions](https://docs.cloud.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm)
* [Configuring Your Tenancy for Function Development](https://docs.cloud.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsuploading.htm)
* [Configuring Your Client Environment for Function Development](https://docs.cloud.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsconfiguringclient.htm#Configuring_Your_Client_Environment_for_Function_Development)

### Generic Function Configuration

### Generic Event Configuration 

### Generic Logging Configuration 

## Additional background information
* [OCI serverless Functions](https://docs.cloud.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm)
* [OCI cloudevents](https://docs.cloud.oracle.com/en-us/iaas/Content/Events/Concepts/eventsoverview.htm)
* [Cloudevents standard](https://cloudevents.io/)
* [Microsoft Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview)
