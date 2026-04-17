# JournalCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**date_time** | **datetime** |  | [optional] 
**parent_journal_id** | **str** |  | [optional] 
**journal_type_id** | **str** |  | [optional] 
**ledger_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.journal_create_dto import JournalCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of JournalCreateDto from a JSON string
journal_create_dto_instance = JournalCreateDto.from_json(json)
# print the JSON string representation of the object
print(JournalCreateDto.to_json())

# convert the object into a dict
journal_create_dto_dict = journal_create_dto_instance.to_dict()
# create an instance of JournalCreateDto from a dict
journal_create_dto_from_dict = JournalCreateDto.from_dict(journal_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


