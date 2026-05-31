# TrainingProgramCourseUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**training_program_id** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.training_program_course_update_dto import TrainingProgramCourseUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramCourseUpdateDto from a JSON string
training_program_course_update_dto_instance = TrainingProgramCourseUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramCourseUpdateDto.to_json())

# convert the object into a dict
training_program_course_update_dto_dict = training_program_course_update_dto_instance.to_dict()
# create an instance of TrainingProgramCourseUpdateDto from a dict
training_program_course_update_dto_from_dict = TrainingProgramCourseUpdateDto.from_dict(training_program_course_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


