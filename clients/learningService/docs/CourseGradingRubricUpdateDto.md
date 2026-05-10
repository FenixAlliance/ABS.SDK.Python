# CourseGradingRubricUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enable_points** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.course_grading_rubric_update_dto import CourseGradingRubricUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradingRubricUpdateDto from a JSON string
course_grading_rubric_update_dto_instance = CourseGradingRubricUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseGradingRubricUpdateDto.to_json())

# convert the object into a dict
course_grading_rubric_update_dto_dict = course_grading_rubric_update_dto_instance.to_dict()
# create an instance of CourseGradingRubricUpdateDto from a dict
course_grading_rubric_update_dto_from_dict = CourseGradingRubricUpdateDto.from_dict(course_grading_rubric_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


