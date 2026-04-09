# JournalUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**date_time** | **datetime** |  | [optional] 
**parent_journal_id** | **str** |  | [optional] 
**journal_type_id** | **str** |  | [optional] 
**ledger_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.journal_update_dto import JournalUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of JournalUpdateDto from a JSON string
journal_update_dto_instance = JournalUpdateDto.from_json(json)
# print the JSON string representation of the object
print(JournalUpdateDto.to_json())

# convert the object into a dict
journal_update_dto_dict = journal_update_dto_instance.to_dict()
# create an instance of JournalUpdateDto from a dict
journal_update_dto_from_dict = JournalUpdateDto.from_dict(journal_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


