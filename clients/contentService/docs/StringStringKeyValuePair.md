# StringStringKeyValuePair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.string_string_key_value_pair import StringStringKeyValuePair

# TODO update the JSON string below
json = "{}"
# create an instance of StringStringKeyValuePair from a JSON string
string_string_key_value_pair_instance = StringStringKeyValuePair.from_json(json)
# print the JSON string representation of the object
print(StringStringKeyValuePair.to_json())

# convert the object into a dict
string_string_key_value_pair_dict = string_string_key_value_pair_instance.to_dict()
# create an instance of StringStringKeyValuePair from a dict
string_string_key_value_pair_from_dict = StringStringKeyValuePair.from_dict(string_string_key_value_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


