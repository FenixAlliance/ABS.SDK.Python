# JournalEntryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**group** | **bool** |  | [optional] 
**opening** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**forex_rates_snapshot** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**credit** | **float** |  | [optional] 
**debit** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**journal_id** | **str** |  | [optional] 
**journal_name** | **str** |  | [optional] 
**journal_code** | **str** |  | [optional] 
**credit_account_id** | **str** |  | [optional] 
**credit_account_name** | **str** |  | [optional] 
**debit_account_id** | **str** |  | [optional] 
**debit_account_name** | **str** |  | [optional] 
**invoice_code** | **str** |  | [optional] 
**parent_journal_entry_id** | **str** |  | [optional] 
**credit_amount** | [**Money**](Money.md) |  | [optional] 
**debit_amount** | [**Money**](Money.md) |  | [optional] 

## Example

```python
from openapi_client.models.journal_entry_dto import JournalEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryDto from a JSON string
journal_entry_dto_instance = JournalEntryDto.from_json(json)
# print the JSON string representation of the object
print(JournalEntryDto.to_json())

# convert the object into a dict
journal_entry_dto_dict = journal_entry_dto_instance.to_dict()
# create an instance of JournalEntryDto from a dict
journal_entry_dto_from_dict = JournalEntryDto.from_dict(journal_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


