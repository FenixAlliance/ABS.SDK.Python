# CountQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**raw_value** | **str** |  | [optional] 
**value** | **bool** |  | [optional] [readonly] 
**validator** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.count_query_option import CountQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of CountQueryOption from a JSON string
count_query_option_instance = CountQueryOption.from_json(json)
# print the JSON string representation of the object
print(CountQueryOption.to_json())

# convert the object into a dict
count_query_option_dict = count_query_option_instance.to_dict()
# create an instance of CountQueryOption from a dict
count_query_option_from_dict = CountQueryOption.from_dict(count_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


