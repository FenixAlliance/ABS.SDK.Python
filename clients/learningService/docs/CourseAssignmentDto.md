# CourseAssignmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instructions** | **str** |  | [optional] 
**points** | **float** |  | [optional] 
**due_date_time** | **datetime** |  | [optional] 
**course_id** | **str** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 
**course_section_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_assignment_dto import CourseAssignmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentDto from a JSON string
course_assignment_dto_instance = CourseAssignmentDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentDto.to_json())

# convert the object into a dict
course_assignment_dto_dict = course_assignment_dto_instance.to_dict()
# create an instance of CourseAssignmentDto from a dict
course_assignment_dto_from_dict = CourseAssignmentDto.from_dict(course_assignment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


