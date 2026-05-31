# ExpenseClaimUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_type_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.expense_claim_update_dto import ExpenseClaimUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseClaimUpdateDto from a JSON string
expense_claim_update_dto_instance = ExpenseClaimUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ExpenseClaimUpdateDto.to_json())

# convert the object into a dict
expense_claim_update_dto_dict = expense_claim_update_dto_instance.to_dict()
# create an instance of ExpenseClaimUpdateDto from a dict
expense_claim_update_dto_from_dict = ExpenseClaimUpdateDto.from_dict(expense_claim_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


