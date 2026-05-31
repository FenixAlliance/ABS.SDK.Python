# SelectExpandQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**raw_select** | **str** |  | [optional] [readonly] 
**raw_expand** | **str** |  | [optional] [readonly] 
**compute** | [**ComputeQueryOption**](ComputeQueryOption.md) |  | [optional] 
**validator** | **object** |  | [optional] 
**select_expand_clause** | [**SelectExpandClause**](SelectExpandClause.md) |  | [optional] 
**levels_max_literal_expansion_depth** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.select_expand_query_option import SelectExpandQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of SelectExpandQueryOption from a JSON string
select_expand_query_option_instance = SelectExpandQueryOption.from_json(json)
# print the JSON string representation of the object
print(SelectExpandQueryOption.to_json())

# convert the object into a dict
select_expand_query_option_dict = select_expand_query_option_instance.to_dict()
# create an instance of SelectExpandQueryOption from a dict
select_expand_query_option_from_dict = SelectExpandQueryOption.from_dict(select_expand_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


