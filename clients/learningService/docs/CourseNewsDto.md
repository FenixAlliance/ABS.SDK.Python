# CourseNewsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_news_dto import CourseNewsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseNewsDto from a JSON string
course_news_dto_instance = CourseNewsDto.from_json(json)
# print the JSON string representation of the object
print(CourseNewsDto.to_json())

# convert the object into a dict
course_news_dto_dict = course_news_dto_instance.to_dict()
# create an instance of CourseNewsDto from a dict
course_news_dto_from_dict = CourseNewsDto.from_dict(course_news_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


