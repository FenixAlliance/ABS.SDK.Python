# TrainingProgramDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.training_program_dto import TrainingProgramDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramDto from a JSON string
training_program_dto_instance = TrainingProgramDto.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramDto.to_json())

# convert the object into a dict
training_program_dto_dict = training_program_dto_instance.to_dict()
# create an instance of TrainingProgramDto from a dict
training_program_dto_from_dict = TrainingProgramDto.from_dict(training_program_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


