# AccountingEntryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | **str** |  | 
**var_date** | **datetime** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency_id** | **str** |  | 
**debit_account_id** | **str** |  | [optional] 
**credit_account_id** | **str** |  | [optional] 
**journal_entry_id** | **str** |  | [optional] 
**accounting_entry_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.accounting_entry_create_dto import AccountingEntryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingEntryCreateDto from a JSON string
accounting_entry_create_dto_instance = AccountingEntryCreateDto.from_json(json)
# print the JSON string representation of the object
print(AccountingEntryCreateDto.to_json())

# convert the object into a dict
accounting_entry_create_dto_dict = accounting_entry_create_dto_instance.to_dict()
# create an instance of AccountingEntryCreateDto from a dict
accounting_entry_create_dto_from_dict = AccountingEntryCreateDto.from_dict(accounting_entry_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


