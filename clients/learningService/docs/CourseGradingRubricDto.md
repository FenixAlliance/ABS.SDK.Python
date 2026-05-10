# CourseGradingRubricDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enable_points** | **bool** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_grading_rubric_dto import CourseGradingRubricDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradingRubricDto from a JSON string
course_grading_rubric_dto_instance = CourseGradingRubricDto.from_json(json)
# print the JSON string representation of the object
print(CourseGradingRubricDto.to_json())

# convert the object into a dict
course_grading_rubric_dto_dict = course_grading_rubric_dto_instance.to_dict()
# create an instance of CourseGradingRubricDto from a dict
course_grading_rubric_dto_from_dict = CourseGradingRubricDto.from_dict(course_grading_rubric_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


