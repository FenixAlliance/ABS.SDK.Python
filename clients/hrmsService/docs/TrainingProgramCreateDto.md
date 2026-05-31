# TrainingProgramCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.training_program_create_dto import TrainingProgramCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramCreateDto from a JSON string
training_program_create_dto_instance = TrainingProgramCreateDto.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramCreateDto.to_json())

# convert the object into a dict
training_program_create_dto_dict = training_program_create_dto_instance.to_dict()
# create an instance of TrainingProgramCreateDto from a dict
training_program_create_dto_from_dict = TrainingProgramCreateDto.from_dict(training_program_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


