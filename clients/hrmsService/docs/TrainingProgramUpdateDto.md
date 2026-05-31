# TrainingProgramUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.training_program_update_dto import TrainingProgramUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramUpdateDto from a JSON string
training_program_update_dto_instance = TrainingProgramUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramUpdateDto.to_json())

# convert the object into a dict
training_program_update_dto_dict = training_program_update_dto_instance.to_dict()
# create an instance of TrainingProgramUpdateDto from a dict
training_program_update_dto_from_dict = TrainingProgramUpdateDto.from_dict(training_program_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


