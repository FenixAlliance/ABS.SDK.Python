# TopQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**raw_value** | **str** |  | [optional] 
**value** | **int** |  | [optional] [readonly] 
**validator** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.top_query_option import TopQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of TopQueryOption from a JSON string
top_query_option_instance = TopQueryOption.from_json(json)
# print the JSON string representation of the object
print(TopQueryOption.to_json())

# convert the object into a dict
top_query_option_dict = top_query_option_instance.to_dict()
# create an instance of TopQueryOption from a dict
top_query_option_from_dict = TopQueryOption.from_dict(top_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


