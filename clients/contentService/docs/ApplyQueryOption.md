# ApplyQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**result_clr_type** | [**Type**](Type.md) |  | [optional] 
**apply_clause** | [**ApplyClause**](ApplyClause.md) |  | [optional] 
**raw_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.apply_query_option import ApplyQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyQueryOption from a JSON string
apply_query_option_instance = ApplyQueryOption.from_json(json)
# print the JSON string representation of the object
print(ApplyQueryOption.to_json())

# convert the object into a dict
apply_query_option_dict = apply_query_option_instance.to_dict()
# create an instance of ApplyQueryOption from a dict
apply_query_option_from_dict = ApplyQueryOption.from_dict(apply_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


