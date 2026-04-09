# CourseFileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**file_upload_url** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**file_length** | **int** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_file_dto import CourseFileDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseFileDto from a JSON string
course_file_dto_instance = CourseFileDto.from_json(json)
# print the JSON string representation of the object
print(CourseFileDto.to_json())

# convert the object into a dict
course_file_dto_dict = course_file_dto_instance.to_dict()
# create an instance of CourseFileDto from a dict
course_file_dto_from_dict = CourseFileDto.from_dict(course_file_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


