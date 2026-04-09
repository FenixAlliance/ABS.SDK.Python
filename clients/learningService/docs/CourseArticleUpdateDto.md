# CourseArticleUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_article_update_dto import CourseArticleUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseArticleUpdateDto from a JSON string
course_article_update_dto_instance = CourseArticleUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseArticleUpdateDto.to_json())

# convert the object into a dict
course_article_update_dto_dict = course_article_update_dto_instance.to_dict()
# create an instance of CourseArticleUpdateDto from a dict
course_article_update_dto_from_dict = CourseArticleUpdateDto.from_dict(course_article_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


