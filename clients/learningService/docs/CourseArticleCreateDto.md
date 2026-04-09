# CourseArticleCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**course_id** | **str** |  | 
**course_wiki_id** | **str** |  | 
**business_id** | **str** |  | 

## Example

```python
from openapi_client.models.course_article_create_dto import CourseArticleCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseArticleCreateDto from a JSON string
course_article_create_dto_instance = CourseArticleCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseArticleCreateDto.to_json())

# convert the object into a dict
course_article_create_dto_dict = course_article_create_dto_instance.to_dict()
# create an instance of CourseArticleCreateDto from a dict
course_article_create_dto_from_dict = CourseArticleCreateDto.from_dict(course_article_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


