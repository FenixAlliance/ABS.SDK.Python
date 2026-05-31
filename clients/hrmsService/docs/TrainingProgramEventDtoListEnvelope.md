# TrainingProgramEventDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TrainingProgramEventDto]**](TrainingProgramEventDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.training_program_event_dto_list_envelope import TrainingProgramEventDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramEventDtoListEnvelope from a JSON string
training_program_event_dto_list_envelope_instance = TrainingProgramEventDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramEventDtoListEnvelope.to_json())

# convert the object into a dict
training_program_event_dto_list_envelope_dict = training_program_event_dto_list_envelope_instance.to_dict()
# create an instance of TrainingProgramEventDtoListEnvelope from a dict
training_program_event_dto_list_envelope_from_dict = TrainingProgramEventDtoListEnvelope.from_dict(training_program_event_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


