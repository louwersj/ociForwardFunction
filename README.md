# ociForwardFunction - Event and Log integration for Oracle Cloud

ociForwardFunction is a collection of functions used to integrate Oracle Cloud - OCI - with third party solutions. The primary initial use case is (has been) integrating Oracle Cloud logging and CNCF compatible Oracle Cloud Events. For the creation of the integrations OCI functions are used and written primarily in Python to leverage the concept of clud native serverless as much as possible and to ensure an ease of deployment and use for users. 

It is expected that the person implementing one or mulitple of the functions provided by the ociForwardFunction has a basic understanding of OCI, OCI events and the target(s) that are intended for this integration.  

## Integrations

### OCI Cloud Events towards MS Azure Sentinel
Sending OCI Cloud Events to Micorsoft Azure Sentinel for inclusion in a Azure Sentinel log workspace. This can be achieved by using the ociCloudEvents2azureSentinel functionalitly. [Documentation](ociCloudEvents2azureSentinel/README.md)

*Tested = Yes, Operational = Yes*

### OCI logging towards MS Azure Sentinel
Sending OCI logging to Micorsoft Azure Sentinel for inclusion in a Azure Sentinel log workspace. This can be achieved by using the ociLogging2azureSentinel functionalitly.

*Tested = No, Operational = No*

## Deployment and configuration

### Generic Function Deployment

### Generic Function Configuration

### Generic Event Configuration 

## Additional background information
* [OCI serverless Functions](https://docs.cloud.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm)
* [OCI cloudevents](https://docs.cloud.oracle.com/en-us/iaas/Content/Events/Concepts/eventsoverview.htm)
* [Cloudevents standard](https://cloudevents.io/)
* [Microsoft Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview)
