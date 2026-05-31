# TrainingProgramCourseCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**training_program_id** | **str** |  | 
**course_id** | **str** |  | 

## Example

```python
from openapi_client.models.training_program_course_create_dto import TrainingProgramCourseCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramCourseCreateDto from a JSON string
training_program_course_create_dto_instance = TrainingProgramCourseCreateDto.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramCourseCreateDto.to_json())

# convert the object into a dict
training_program_course_create_dto_dict = training_program_course_create_dto_instance.to_dict()
# create an instance of TrainingProgramCourseCreateDto from a dict
training_program_course_create_dto_from_dict = TrainingProgramCourseCreateDto.from_dict(training_program_course_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


