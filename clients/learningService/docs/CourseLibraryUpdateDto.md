# CourseLibraryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_library_update_dto import CourseLibraryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseLibraryUpdateDto from a JSON string
course_library_update_dto_instance = CourseLibraryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseLibraryUpdateDto.to_json())

# convert the object into a dict
course_library_update_dto_dict = course_library_update_dto_instance.to_dict()
# create an instance of CourseLibraryUpdateDto from a dict
course_library_update_dto_from_dict = CourseLibraryUpdateDto.from_dict(course_library_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


