# JournalEntryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**group** | **bool** |  | [optional] 
**opening** | **bool** |  | [optional] 
**description** | **str** |  | 
**var_date** | **datetime** |  | 
**debit** | **float** |  | [optional] 
**credit** | **float** |  | [optional] 
**journal_id** | **str** |  | 
**currency_id** | **str** |  | 
**debit_account_id** | **str** |  | 
**credit_account_id** | **str** |  | 
**parent_journal_entry_id** | **str** |  | [optional] 
**invoice_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.journal_entry_create_dto import JournalEntryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryCreateDto from a JSON string
journal_entry_create_dto_instance = JournalEntryCreateDto.from_json(json)
# print the JSON string representation of the object
print(JournalEntryCreateDto.to_json())

# convert the object into a dict
journal_entry_create_dto_dict = journal_entry_create_dto_instance.to_dict()
# create an instance of JournalEntryCreateDto from a dict
journal_entry_create_dto_from_dict = JournalEntryCreateDto.from_dict(journal_entry_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


