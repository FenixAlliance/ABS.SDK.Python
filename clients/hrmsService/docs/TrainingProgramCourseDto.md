# TrainingProgramCourseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**training_program_id** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.training_program_course_dto import TrainingProgramCourseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramCourseDto from a JSON string
training_program_course_dto_instance = TrainingProgramCourseDto.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramCourseDto.to_json())

# convert the object into a dict
training_program_course_dto_dict = training_program_course_dto_instance.to_dict()
# create an instance of TrainingProgramCourseDto from a dict
training_program_course_dto_from_dict = TrainingProgramCourseDto.from_dict(training_program_course_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


