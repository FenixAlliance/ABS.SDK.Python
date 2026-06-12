# OrderByQueryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ODataQueryContext**](ODataQueryContext.md) |  | [optional] 
**order_by_nodes** | [**List[OrderByNode]**](OrderByNode.md) |  | [optional] [readonly] 
**raw_value** | **str** |  | [optional] 
**validator** | **object** |  | [optional] 
**compute** | [**ComputeQueryOption**](ComputeQueryOption.md) |  | [optional] 
**order_by_clause** | [**OrderByClause**](OrderByClause.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_by_query_option import OrderByQueryOption

# TODO update the JSON string below
json = "{}"
# create an instance of OrderByQueryOption from a JSON string
order_by_query_option_instance = OrderByQueryOption.from_json(json)
# print the JSON string representation of the object
print(OrderByQueryOption.to_json())

# convert the object into a dict
order_by_query_option_dict = order_by_query_option_instance.to_dict()
# create an instance of OrderByQueryOption from a dict
order_by_query_option_from_dict = OrderByQueryOption.from_dict(order_by_query_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


