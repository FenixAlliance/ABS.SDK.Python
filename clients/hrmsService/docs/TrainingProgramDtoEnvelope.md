# TrainingProgramDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TrainingProgramDto**](TrainingProgramDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.training_program_dto_envelope import TrainingProgramDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramDtoEnvelope from a JSON string
training_program_dto_envelope_instance = TrainingProgramDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramDtoEnvelope.to_json())

# convert the object into a dict
training_program_dto_envelope_dict = training_program_dto_envelope_instance.to_dict()
# create an instance of TrainingProgramDtoEnvelope from a dict
training_program_dto_envelope_from_dict = TrainingProgramDtoEnvelope.from_dict(training_program_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


