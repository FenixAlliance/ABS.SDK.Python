# QueryString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**has_value** | **bool** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.query_string import QueryString

# TODO update the JSON string below
json = "{}"
# create an instance of QueryString from a JSON string
query_string_instance = QueryString.from_json(json)
# print the JSON string representation of the object
print(QueryString.to_json())

# convert the object into a dict
query_string_dict = query_string_instance.to_dict()
# create an instance of QueryString from a dict
query_string_from_dict = QueryString.from_dict(query_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


