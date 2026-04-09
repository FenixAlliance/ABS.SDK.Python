# BudgetAccountEntryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**description** | **str** |  | 
**var_date** | **datetime** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency_id** | **str** |  | 
**debit_account_id** | **str** |  | [optional] 
**credit_account_id** | **str** |  | [optional] 
**journal_entry_id** | **str** |  | [optional] 
**accounting_entry_type** | **str** |  | [optional] 
**budget_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.budget_account_entry_create_dto import BudgetAccountEntryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetAccountEntryCreateDto from a JSON string
budget_account_entry_create_dto_instance = BudgetAccountEntryCreateDto.from_json(json)
# print the JSON string representation of the object
print(BudgetAccountEntryCreateDto.to_json())

# convert the object into a dict
budget_account_entry_create_dto_dict = budget_account_entry_create_dto_instance.to_dict()
# create an instance of BudgetAccountEntryCreateDto from a dict
budget_account_entry_create_dto_from_dict = BudgetAccountEntryCreateDto.from_dict(budget_account_entry_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


