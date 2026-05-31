# DefaultQueryConfigurations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_expand** | **bool** |  | [optional] 
**enable_select** | **bool** |  | [optional] 
**enable_count** | **bool** |  | [optional] 
**enable_order_by** | **bool** |  | [optional] 
**enable_filter** | **bool** |  | [optional] 
**max_top** | **int** |  | [optional] 
**enable_skip_token** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.default_query_configurations import DefaultQueryConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultQueryConfigurations from a JSON string
default_query_configurations_instance = DefaultQueryConfigurations.from_json(json)
# print the JSON string representation of the object
print(DefaultQueryConfigurations.to_json())

# convert the object into a dict
default_query_configurations_dict = default_query_configurations_instance.to_dict()
# create an instance of DefaultQueryConfigurations from a dict
default_query_configurations_from_dict = DefaultQueryConfigurations.from_dict(default_query_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


