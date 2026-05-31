# OrderByClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**then_by** | [**OrderByClause**](OrderByClause.md) |  | [optional] 
**expression** | [**SingleValueNode**](SingleValueNode.md) |  | [optional] 
**direction** | **str** |  | [optional] 
**range_variable** | [**RangeVariable**](RangeVariable.md) |  | [optional] 
**item_type** | [**IEdmTypeReference**](IEdmTypeReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_by_clause import OrderByClause

# TODO update the JSON string below
json = "{}"
# create an instance of OrderByClause from a JSON string
order_by_clause_instance = OrderByClause.from_json(json)
# print the JSON string representation of the object
print(OrderByClause.to_json())

# convert the object into a dict
order_by_clause_dict = order_by_clause_instance.to_dict()
# create an instance of OrderByClause from a dict
order_by_clause_from_dict = OrderByClause.from_dict(order_by_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


