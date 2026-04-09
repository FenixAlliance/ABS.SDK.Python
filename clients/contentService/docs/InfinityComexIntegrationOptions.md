# InfinityComexIntegrationOptions


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
from openapi_client.models.infinity_comex_integration_options import InfinityComexIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of InfinityComexIntegrationOptions from a JSON string
infinity_comex_integration_options_instance = InfinityComexIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(InfinityComexIntegrationOptions.to_json())

# convert the object into a dict
infinity_comex_integration_options_dict = infinity_comex_integration_options_instance.to_dict()
# create an instance of InfinityComexIntegrationOptions from a dict
infinity_comex_integration_options_from_dict = InfinityComexIntegrationOptions.from_dict(infinity_comex_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


