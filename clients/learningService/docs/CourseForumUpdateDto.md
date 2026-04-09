# CourseForumUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_forum_update_dto import CourseForumUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseForumUpdateDto from a JSON string
course_forum_update_dto_instance = CourseForumUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseForumUpdateDto.to_json())

# convert the object into a dict
course_forum_update_dto_dict = course_forum_update_dto_instance.to_dict()
# create an instance of CourseForumUpdateDto from a dict
course_forum_update_dto_from_dict = CourseForumUpdateDto.from_dict(course_forum_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


