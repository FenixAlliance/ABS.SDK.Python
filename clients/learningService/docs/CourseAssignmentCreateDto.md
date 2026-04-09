# CourseAssignmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**instructions** | **str** |  | [optional] 
**points** | **float** |  | [optional] 
**course_id** | **str** |  | 
**business_id** | **str** |  | 
**course_unit_id** | **str** |  | [optional] 
**course_cohort_id** | **str** |  | [optional] 
**course_assignment_type_id** | **str** |  | [optional] 
**due_date_time** | **datetime** |  | [optional] 
**asign_to_all_cohorts** | **bool** |  | [optional] 
**resources** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_assignment_create_dto import CourseAssignmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentCreateDto from a JSON string
course_assignment_create_dto_instance = CourseAssignmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentCreateDto.to_json())

# convert the object into a dict
course_assignment_create_dto_dict = course_assignment_create_dto_instance.to_dict()
# create an instance of CourseAssignmentCreateDto from a dict
course_assignment_create_dto_from_dict = CourseAssignmentCreateDto.from_dict(course_assignment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


