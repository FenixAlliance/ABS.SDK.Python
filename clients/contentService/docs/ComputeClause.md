# ComputeClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computed_items** | [**List[ComputeExpression]**](ComputeExpression.md) |  | [optional] 

## Example

```python
from openapi_client.models.compute_clause import ComputeClause

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeClause from a JSON string
compute_clause_instance = ComputeClause.from_json(json)
# print the JSON string representation of the object
print(ComputeClause.to_json())

# convert the object into a dict
compute_clause_dict = compute_clause_instance.to_dict()
# create an instance of ComputeClause from a dict
compute_clause_from_dict = ComputeClause.from_dict(compute_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


