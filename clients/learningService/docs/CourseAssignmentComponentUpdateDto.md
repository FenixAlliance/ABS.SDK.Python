# CourseAssignmentComponentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**course_assignment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_assignment_component_update_dto import CourseAssignmentComponentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentComponentUpdateDto from a JSON string
course_assignment_component_update_dto_instance = CourseAssignmentComponentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentComponentUpdateDto.to_json())

# convert the object into a dict
course_assignment_component_update_dto_dict = course_assignment_component_update_dto_instance.to_dict()
# create an instance of CourseAssignmentComponentUpdateDto from a dict
course_assignment_component_update_dto_from_dict = CourseAssignmentComponentUpdateDto.from_dict(course_assignment_component_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


