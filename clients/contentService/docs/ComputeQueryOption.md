# ComputeQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**result_clr_type** | [**Type**](Type.md) |  | [optional] 
**compute_clause** | [**ComputeClause**](ComputeClause.md) |  | [optional] 
**raw_value** | **str** |  | [optional] 
**validator** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.compute_query_option import ComputeQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeQueryOption from a JSON string
compute_query_option_instance = ComputeQueryOption.from_json(json)
# print the JSON string representation of the object
print(ComputeQueryOption.to_json())

# convert the object into a dict
compute_query_option_dict = compute_query_option_instance.to_dict()
# create an instance of ComputeQueryOption from a dict
compute_query_option_from_dict = ComputeQueryOption.from_dict(compute_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


