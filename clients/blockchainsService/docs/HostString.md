# HostString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**has_value** | **bool** |  | [optional] [readonly] 
**host** | **str** |  | [optional] [readonly] 
**port** | **int** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.host_string import HostString

# TODO update the JSON string below
json = "{}"
# create an instance of HostString from a JSON string
host_string_instance = HostString.from_json(json)
# print the JSON string representation of the object
print(HostString.to_json())

# convert the object into a dict
host_string_dict = host_string_instance.to_dict()
# create an instance of HostString from a dict
host_string_from_dict = HostString.from_dict(host_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


