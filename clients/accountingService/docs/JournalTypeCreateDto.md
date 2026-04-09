# JournalTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.journal_type_create_dto import JournalTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of JournalTypeCreateDto from a JSON string
journal_type_create_dto_instance = JournalTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(JournalTypeCreateDto.to_json())

# convert the object into a dict
journal_type_create_dto_dict = journal_type_create_dto_instance.to_dict()
# create an instance of JournalTypeCreateDto from a dict
journal_type_create_dto_from_dict = JournalTypeCreateDto.from_dict(journal_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


