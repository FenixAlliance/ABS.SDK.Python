# AccountingEntryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**debit_account_id** | **str** |  | [optional] 
**credit_account_id** | **str** |  | [optional] 
**journal_entry_id** | **str** |  | [optional] 
**accounting_entry_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.accounting_entry_update_dto import AccountingEntryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingEntryUpdateDto from a JSON string
accounting_entry_update_dto_instance = AccountingEntryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AccountingEntryUpdateDto.to_json())

# convert the object into a dict
accounting_entry_update_dto_dict = accounting_entry_update_dto_instance.to_dict()
# create an instance of AccountingEntryUpdateDto from a dict
accounting_entry_update_dto_from_dict = AccountingEntryUpdateDto.from_dict(accounting_entry_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


