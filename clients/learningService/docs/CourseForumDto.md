# CourseForumDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_forum_dto import CourseForumDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseForumDto from a JSON string
course_forum_dto_instance = CourseForumDto.from_json(json)
# print the JSON string representation of the object
print(CourseForumDto.to_json())

# convert the object into a dict
course_forum_dto_dict = course_forum_dto_instance.to_dict()
# create an instance of CourseForumDto from a dict
course_forum_dto_from_dict = CourseForumDto.from_dict(course_forum_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


