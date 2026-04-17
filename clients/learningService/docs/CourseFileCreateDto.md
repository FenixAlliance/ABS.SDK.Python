# CourseFileCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**file_name** | **str** |  | 
**file_upload_url** | **str** |  | 
**content_type** | **str** |  | [optional] 
**file_length** | **int** |  | [optional] 
**course_id** | **str** |  | 

## Example

```python
from openapi_client.models.course_file_create_dto import CourseFileCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseFileCreateDto from a JSON string
course_file_create_dto_instance = CourseFileCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseFileCreateDto.to_json())

# convert the object into a dict
course_file_create_dto_dict = course_file_create_dto_instance.to_dict()
# create an instance of CourseFileCreateDto from a dict
course_file_create_dto_from_dict = CourseFileCreateDto.from_dict(course_file_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


