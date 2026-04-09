# JournalTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**JournalTypeDto**](JournalTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.journal_type_dto_envelope import JournalTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of JournalTypeDtoEnvelope from a JSON string
journal_type_dto_envelope_instance = JournalTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(JournalTypeDtoEnvelope.to_json())

# convert the object into a dict
journal_type_dto_envelope_dict = journal_type_dto_envelope_instance.to_dict()
# create an instance of JournalTypeDtoEnvelope from a dict
journal_type_dto_envelope_from_dict = JournalTypeDtoEnvelope.from_dict(journal_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


