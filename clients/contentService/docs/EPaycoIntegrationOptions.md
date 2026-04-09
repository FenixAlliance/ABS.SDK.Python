# EPaycoIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer_key** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**api_secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.e_payco_integration_options import EPaycoIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EPaycoIntegrationOptions from a JSON string
e_payco_integration_options_instance = EPaycoIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(EPaycoIntegrationOptions.to_json())

# convert the object into a dict
e_payco_integration_options_dict = e_payco_integration_options_instance.to_dict()
# create an instance of EPaycoIntegrationOptions from a dict
e_payco_integration_options_from_dict = EPaycoIntegrationOptions.from_dict(e_payco_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


