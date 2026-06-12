# ComputeExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**SingleValueNode**](SingleValueNode.md) |  | [optional] 
**alias** | **str** |  | [optional] 
**type_reference** | [**IEdmTypeReference**](IEdmTypeReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.compute_expression import ComputeExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeExpression from a JSON string
compute_expression_instance = ComputeExpression.from_json(json)
# print the JSON string representation of the object
print(ComputeExpression.to_json())

# convert the object into a dict
compute_expression_dict = compute_expression_instance.to_dict()
# create an instance of ComputeExpression from a dict
compute_expression_from_dict = ComputeExpression.from_dict(compute_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


