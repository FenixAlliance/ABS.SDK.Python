# SearchQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**result_clr_type** | [**Type**](Type.md) |  | [optional] 
**search_clause** | [**SearchClause**](SearchClause.md) |  | [optional] 
**raw_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.search_query_option import SearchQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of SearchQueryOption from a JSON string
search_query_option_instance = SearchQueryOption.from_json(json)
# print the JSON string representation of the object
print(SearchQueryOption.to_json())

# convert the object into a dict
search_query_option_dict = search_query_option_instance.to_dict()
# create an instance of SearchQueryOption from a dict
search_query_option_from_dict = SearchQueryOption.from_dict(search_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


