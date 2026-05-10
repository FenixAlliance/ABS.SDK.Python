# CourseAssignmentTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**abbreviation** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**excluded** | **int** |  | [optional] 
**course_id** | **str** |  | 

## Example

```python
from openapi_client.models.course_assignment_type_create_dto import CourseAssignmentTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAssignmentTypeCreateDto from a JSON string
course_assignment_type_create_dto_instance = CourseAssignmentTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseAssignmentTypeCreateDto.to_json())

# convert the object into a dict
course_assignment_type_create_dto_dict = course_assignment_type_create_dto_instance.to_dict()
# create an instance of CourseAssignmentTypeCreateDto from a dict
course_assignment_type_create_dto_from_dict = CourseAssignmentTypeCreateDto.from_dict(course_assignment_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


