# ociForwardFunction

ociForwardFunction is a collection of functions used to integrate Oracle CLoud - OCI - with third party solutions. The primary initial use case is (has been) integrating Oracle Cloud logging and CNCF compatible Cloud Events. For the creation of the integrations OCI functions are used and written primarily in Python. 

## integrations

### OCI Cloud Events towards MS Azure Sentinel
Sending OCI Cloud Events to Micorsoft Azure Sentinel for inclusion in a Azure Sentinel log workspace. This can be achieved by using the ociCloudEvents2azureSentinel functionalitly.

Tested = Yes
Operational = Yes

### OCI logging towards MS Azure Sentinel
Sending OCI logging to Micorsoft Azure Sentinel for inclusion in a Azure Sentinel log workspace. This can be achieved by using the ociLogging2azureSentinel functionalitly.

Tested = No
Operational = No

## Additional background information
* [OCI serverless Functions](https://docs.cloud.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm)
* [OCI cloudevents](https://docs.cloud.oracle.com/en-us/iaas/Content/Events/Concepts/eventsoverview.htm)
* [Cloudevents standard](https://cloudevents.io/)
