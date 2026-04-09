# JournalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**ledger_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 
**journal_type_id** | **str** |  | [optional] 
**parent_journal_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.journal_dto import JournalDto

# TODO update the JSON string below
json = "{}"
# create an instance of JournalDto from a JSON string
journal_dto_instance = JournalDto.from_json(json)
# print the JSON string representation of the object
print(JournalDto.to_json())

# convert the object into a dict
journal_dto_dict = journal_dto_instance.to_dict()
# create an instance of JournalDto from a dict
journal_dto_from_dict = JournalDto.from_dict(journal_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


