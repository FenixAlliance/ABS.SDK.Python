# CourseAssignmentTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**excluded** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.course_assignment_type_update_dto import CourseAssignmentTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentTypeUpdateDto from a JSON string
course_assignment_type_update_dto_instance = CourseAssignmentTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentTypeUpdateDto.to_json())

# convert the object into a dict
course_assignment_type_update_dto_dict = course_assignment_type_update_dto_instance.to_dict()
# create an instance of CourseAssignmentTypeUpdateDto from a dict
course_assignment_type_update_dto_from_dict = CourseAssignmentTypeUpdateDto.from_dict(course_assignment_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


