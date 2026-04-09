# JournalDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[JournalDto]**](JournalDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.journal_dto_i_read_only_list_envelope import JournalDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of JournalDtoIReadOnlyListEnvelope from a JSON string
journal_dto_i_read_only_list_envelope_instance = JournalDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(JournalDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
journal_dto_i_read_only_list_envelope_dict = journal_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of JournalDtoIReadOnlyListEnvelope from a dict
journal_dto_i_read_only_list_envelope_from_dict = JournalDtoIReadOnlyListEnvelope.from_dict(journal_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


