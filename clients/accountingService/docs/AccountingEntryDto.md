# AccountingEntryDto


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

## Example

```python
from openapi_client.models.accounting_entry_dto import AccountingEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingEntryDto from a JSON string
accounting_entry_dto_instance = AccountingEntryDto.from_json(json)
# print the JSON string representation of the object
print(AccountingEntryDto.to_json())

# convert the object into a dict
accounting_entry_dto_dict = accounting_entry_dto_instance.to_dict()
# create an instance of AccountingEntryDto from a dict
accounting_entry_dto_from_dict = AccountingEntryDto.from_dict(accounting_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


