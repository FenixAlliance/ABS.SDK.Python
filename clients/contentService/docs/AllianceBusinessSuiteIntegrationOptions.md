# AllianceBusinessSuiteIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**app_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.alliance_business_suite_integration_options import AllianceBusinessSuiteIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AllianceBusinessSuiteIntegrationOptions from a JSON string
alliance_business_suite_integration_options_instance = AllianceBusinessSuiteIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(AllianceBusinessSuiteIntegrationOptions.to_json())

# convert the object into a dict
alliance_business_suite_integration_options_dict = alliance_business_suite_integration_options_instance.to_dict()
# create an instance of AllianceBusinessSuiteIntegrationOptions from a dict
alliance_business_suite_integration_options_from_dict = AllianceBusinessSuiteIntegrationOptions.from_dict(alliance_business_suite_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


