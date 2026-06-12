# SkipTokenQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_value** | **str** |  | [optional] 
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**validator** | **object** |  | [optional] 
**handler** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.skip_token_query_option import SkipTokenQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of SkipTokenQueryOption from a JSON string
skip_token_query_option_instance = SkipTokenQueryOption.from_json(json)
# print the JSON string representation of the object
print(SkipTokenQueryOption.to_json())

# convert the object into a dict
skip_token_query_option_dict = skip_token_query_option_instance.to_dict()
# create an instance of SkipTokenQueryOption from a dict
skip_token_query_option_from_dict = SkipTokenQueryOption.from_dict(skip_token_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


