# SkipQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**raw_value** | **str** |  | [optional] 
**value** | **int** |  | [optional] [readonly] 
**validator** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.skip_query_option import SkipQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of SkipQueryOption from a JSON string
skip_query_option_instance = SkipQueryOption.from_json(json)
# print the JSON string representation of the object
print(SkipQueryOption.to_json())

# convert the object into a dict
skip_query_option_dict = skip_query_option_instance.to_dict()
# create an instance of SkipQueryOption from a dict
skip_query_option_from_dict = SkipQueryOption.from_dict(skip_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


