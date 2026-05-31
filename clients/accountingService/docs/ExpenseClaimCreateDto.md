# ExpenseClaimCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**expense_type_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.expense_claim_create_dto import ExpenseClaimCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseClaimCreateDto from a JSON string
expense_claim_create_dto_instance = ExpenseClaimCreateDto.from_json(json)
# print the JSON string representation of the object
print(ExpenseClaimCreateDto.to_json())

# convert the object into a dict
expense_claim_create_dto_dict = expense_claim_create_dto_instance.to_dict()
# create an instance of ExpenseClaimCreateDto from a dict
expense_claim_create_dto_from_dict = ExpenseClaimCreateDto.from_dict(expense_claim_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


