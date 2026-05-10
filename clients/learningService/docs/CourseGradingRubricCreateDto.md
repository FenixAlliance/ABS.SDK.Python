# CourseGradingRubricCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**enable_points** | **bool** |  | [optional] 
**course_id** | **str** |  | 

## Example

```python
from openapi_client.models.course_grading_rubric_create_dto import CourseGradingRubricCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradingRubricCreateDto from a JSON string
course_grading_rubric_create_dto_instance = CourseGradingRubricCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseGradingRubricCreateDto.to_json())

# convert the object into a dict
course_grading_rubric_create_dto_dict = course_grading_rubric_create_dto_instance.to_dict()
# create an instance of CourseGradingRubricCreateDto from a dict
course_grading_rubric_create_dto_from_dict = CourseGradingRubricCreateDto.from_dict(course_grading_rubric_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


