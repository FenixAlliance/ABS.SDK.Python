# BudgetAccountEntryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**debit** | **float** |  | [optional] 
**credit** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**account_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**debit_account_id** | **str** |  | [optional] 
**credit_account_id** | **str** |  | [optional] 
**journal_entry_id** | **str** |  | [optional] 
**debit_account_name** | **str** |  | [optional] 
**credit_account_name** | **str** |  | [optional] 
**accounting_entry_type** | **str** |  | [optional] 
**debit_amount** | [**Money**](Money.md) |  | [optional] 
**credit_amount** | [**Money**](Money.md) |  | [optional] 
**budget_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.budget_account_entry_dto import BudgetAccountEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetAccountEntryDto from a JSON string
budget_account_entry_dto_instance = BudgetAccountEntryDto.from_json(json)
# print the JSON string representation of the object
print(BudgetAccountEntryDto.to_json())

# convert the object into a dict
budget_account_entry_dto_dict = budget_account_entry_dto_instance.to_dict()
# create an instance of BudgetAccountEntryDto from a dict
budget_account_entry_dto_from_dict = BudgetAccountEntryDto.from_dict(budget_account_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


