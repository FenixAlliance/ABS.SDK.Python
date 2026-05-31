# ExpenseClaimDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**expense_type_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.expense_claim_dto import ExpenseClaimDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseClaimDto from a JSON string
expense_claim_dto_instance = ExpenseClaimDto.from_json(json)
# print the JSON string representation of the object
print(ExpenseClaimDto.to_json())

# convert the object into a dict
expense_claim_dto_dict = expense_claim_dto_instance.to_dict()
# create an instance of ExpenseClaimDto from a dict
expense_claim_dto_from_dict = ExpenseClaimDto.from_dict(expense_claim_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


