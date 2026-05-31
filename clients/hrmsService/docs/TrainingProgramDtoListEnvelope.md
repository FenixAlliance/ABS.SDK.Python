# TrainingProgramDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TrainingProgramDto]**](TrainingProgramDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.training_program_dto_list_envelope import TrainingProgramDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramDtoListEnvelope from a JSON string
training_program_dto_list_envelope_instance = TrainingProgramDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramDtoListEnvelope.to_json())

# convert the object into a dict
training_program_dto_list_envelope_dict = training_program_dto_list_envelope_instance.to_dict()
# create an instance of TrainingProgramDtoListEnvelope from a dict
training_program_dto_list_envelope_from_dict = TrainingProgramDtoListEnvelope.from_dict(training_program_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


