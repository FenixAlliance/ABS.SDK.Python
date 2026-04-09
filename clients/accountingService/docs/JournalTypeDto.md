# JournalTypeDto


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
from openapi_client.models.journal_type_dto import JournalTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of JournalTypeDto from a JSON string
journal_type_dto_instance = JournalTypeDto.from_json(json)
# print the JSON string representation of the object
print(JournalTypeDto.to_json())

# convert the object into a dict
journal_type_dto_dict = journal_type_dto_instance.to_dict()
# create an instance of JournalTypeDto from a dict
journal_type_dto_from_dict = JournalTypeDto.from_dict(journal_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


