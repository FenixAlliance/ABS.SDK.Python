# KeySizes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_size** | **int** |  | [optional] 
**max_size** | **int** |  | [optional] 
**skip_size** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.key_sizes import KeySizes

# TODO update the JSON string below
json = "{}"
# create an instance of KeySizes from a JSON string
key_sizes_instance = KeySizes.from_json(json)
# print the JSON string representation of the object
print(KeySizes.to_json())

# convert the object into a dict
key_sizes_dict = key_sizes_instance.to_dict()
# create an instance of KeySizes from a dict
key_sizes_from_dict = KeySizes.from_dict(key_sizes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


