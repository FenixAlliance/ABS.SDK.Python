# CourseFileUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**file_upload_url** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**file_length** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.course_file_update_dto import CourseFileUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseFileUpdateDto from a JSON string
course_file_update_dto_instance = CourseFileUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseFileUpdateDto.to_json())

# convert the object into a dict
course_file_update_dto_dict = course_file_update_dto_instance.to_dict()
# create an instance of CourseFileUpdateDto from a dict
course_file_update_dto_from_dict = CourseFileUpdateDto.from_dict(course_file_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


