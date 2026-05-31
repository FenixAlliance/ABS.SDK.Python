# SearchClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**SingleValueNode**](SingleValueNode.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_clause import SearchClause

# TODO update the JSON string below
json = "{}"
# create an instance of SearchClause from a JSON string
search_clause_instance = SearchClause.from_json(json)
# print the JSON string representation of the object
print(SearchClause.to_json())

# convert the object into a dict
search_clause_dict = search_clause_instance.to_dict()
# create an instance of SearchClause from a dict
search_clause_from_dict = SearchClause.from_dict(search_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


