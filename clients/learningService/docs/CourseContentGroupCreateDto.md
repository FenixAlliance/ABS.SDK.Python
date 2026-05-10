# CourseContentGroupCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**course_id** | **str** |  | 

## Example

```python
from openapi_client.models.course_content_group_create_dto import CourseContentGroupCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseContentGroupCreateDto from a JSON string
course_content_group_create_dto_instance = CourseContentGroupCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseContentGroupCreateDto.to_json())

# convert the object into a dict
course_content_group_create_dto_dict = course_content_group_create_dto_instance.to_dict()
# create an instance of CourseContentGroupCreateDto from a dict
course_content_group_create_dto_from_dict = CourseContentGroupCreateDto.from_dict(course_content_group_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


