# CourseAssignmentTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**excluded** | **int** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_assignment_type_dto import CourseAssignmentTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentTypeDto from a JSON string
course_assignment_type_dto_instance = CourseAssignmentTypeDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentTypeDto.to_json())

# convert the object into a dict
course_assignment_type_dto_dict = course_assignment_type_dto_instance.to_dict()
# create an instance of CourseAssignmentTypeDto from a dict
course_assignment_type_dto_from_dict = CourseAssignmentTypeDto.from_dict(course_assignment_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


