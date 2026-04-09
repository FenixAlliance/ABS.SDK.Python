# CourseAssignmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instructions** | **str** |  | [optional] 
**points** | **float** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 
**course_cohort_id** | **str** |  | [optional] 
**course_assignment_type_id** | **str** |  | [optional] 
**due_date_time** | **datetime** |  | [optional] 
**asign_to_all_cohorts** | **bool** |  | [optional] 
**resources** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_assignment_update_dto import CourseAssignmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentUpdateDto from a JSON string
course_assignment_update_dto_instance = CourseAssignmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentUpdateDto.to_json())

# convert the object into a dict
course_assignment_update_dto_dict = course_assignment_update_dto_instance.to_dict()
# create an instance of CourseAssignmentUpdateDto from a dict
course_assignment_update_dto_from_dict = CourseAssignmentUpdateDto.from_dict(course_assignment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


