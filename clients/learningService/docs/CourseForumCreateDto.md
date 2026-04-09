# CourseForumCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**course_id** | **str** |  | 
**business_id** | **str** |  | 

## Example

```python
from openapi_client.models.course_forum_create_dto import CourseForumCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseForumCreateDto from a JSON string
course_forum_create_dto_instance = CourseForumCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseForumCreateDto.to_json())

# convert the object into a dict
course_forum_create_dto_dict = course_forum_create_dto_instance.to_dict()
# create an instance of CourseForumCreateDto from a dict
course_forum_create_dto_from_dict = CourseForumCreateDto.from_dict(course_forum_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


