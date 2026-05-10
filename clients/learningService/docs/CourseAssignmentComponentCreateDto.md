# CourseAssignmentComponentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**course_assignment_id** | **str** |  | 
**course_id** | **str** |  | 

## Example

```python
from openapi_client.models.course_assignment_component_create_dto import CourseAssignmentComponentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentComponentCreateDto from a JSON string
course_assignment_component_create_dto_instance = CourseAssignmentComponentCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentComponentCreateDto.to_json())

# convert the object into a dict
course_assignment_component_create_dto_dict = course_assignment_component_create_dto_instance.to_dict()
# create an instance of CourseAssignmentComponentCreateDto from a dict
course_assignment_component_create_dto_from_dict = CourseAssignmentComponentCreateDto.from_dict(course_assignment_component_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


