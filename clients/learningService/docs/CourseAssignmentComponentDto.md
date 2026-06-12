# CourseAssignmentComponentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**course_assignment_id** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_assignment_component_dto import CourseAssignmentComponentDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentComponentDto from a JSON string
course_assignment_component_dto_instance = CourseAssignmentComponentDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentComponentDto.to_json())

# convert the object into a dict
course_assignment_component_dto_dict = course_assignment_component_dto_instance.to_dict()
# create an instance of CourseAssignmentComponentDto from a dict
course_assignment_component_dto_from_dict = CourseAssignmentComponentDto.from_dict(course_assignment_component_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


