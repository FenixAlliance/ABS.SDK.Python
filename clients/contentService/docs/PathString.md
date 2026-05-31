# PathString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**has_value** | **bool** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.path_string import PathString

# TODO update the JSON string below
json = "{}"
# create an instance of PathString from a JSON string
path_string_instance = PathString.from_json(json)
# print the JSON string representation of the object
print(PathString.to_json())

# convert the object into a dict
path_string_dict = path_string_instance.to_dict()
# create an instance of PathString from a dict
path_string_from_dict = PathString.from_dict(path_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


