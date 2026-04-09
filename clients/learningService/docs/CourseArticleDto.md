# CourseArticleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**course_wiki_id** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_article_dto import CourseArticleDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseArticleDto from a JSON string
course_article_dto_instance = CourseArticleDto.from_json(json)
# print the JSON string representation of the object
print(CourseArticleDto.to_json())

# convert the object into a dict
course_article_dto_dict = course_article_dto_instance.to_dict()
# create an instance of CourseArticleDto from a dict
course_article_dto_from_dict = CourseArticleDto.from_dict(course_article_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


