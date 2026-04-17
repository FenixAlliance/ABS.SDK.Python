# CourseLibraryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**course_id** | **str** |  | 
**course_unit_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_library_create_dto import CourseLibraryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseLibraryCreateDto from a JSON string
course_library_create_dto_instance = CourseLibraryCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseLibraryCreateDto.to_json())

# convert the object into a dict
course_library_create_dto_dict = course_library_create_dto_instance.to_dict()
# create an instance of CourseLibraryCreateDto from a dict
course_library_create_dto_from_dict = CourseLibraryCreateDto.from_dict(course_library_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


