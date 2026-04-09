# CourseLibraryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_library_dto import CourseLibraryDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseLibraryDto from a JSON string
course_library_dto_instance = CourseLibraryDto.from_json(json)
# print the JSON string representation of the object
print(CourseLibraryDto.to_json())

# convert the object into a dict
course_library_dto_dict = course_library_dto_instance.to_dict()
# create an instance of CourseLibraryDto from a dict
course_library_dto_from_dict = CourseLibraryDto.from_dict(course_library_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


