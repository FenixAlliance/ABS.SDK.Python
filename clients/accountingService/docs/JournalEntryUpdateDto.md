# JournalEntryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **bool** |  | [optional] 
**opening** | **bool** |  | [optional] 
**description** | **str** |  | 
**var_date** | **datetime** |  | 
**debit** | **float** |  | [optional] 
**credit** | **float** |  | [optional] 
**journal_id** | **str** |  | 
**currency_id** | **str** |  | 
**invoice_code** | **str** |  | [optional] 
**debit_account_id** | **str** |  | 
**credit_account_id** | **str** |  | 
**parent_journal_entry_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.journal_entry_update_dto import JournalEntryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryUpdateDto from a JSON string
journal_entry_update_dto_instance = JournalEntryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(JournalEntryUpdateDto.to_json())

# convert the object into a dict
journal_entry_update_dto_dict = journal_entry_update_dto_instance.to_dict()
# create an instance of JournalEntryUpdateDto from a dict
journal_entry_update_dto_from_dict = JournalEntryUpdateDto.from_dict(journal_entry_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


