# CourseNewsCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**course_id** | **str** |  | 
**business_id** | **str** |  | 

## Example

```python
from openapi_client.models.course_news_create_dto import CourseNewsCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseNewsCreateDto from a JSON string
course_news_create_dto_instance = CourseNewsCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseNewsCreateDto.to_json())

# convert the object into a dict
course_news_create_dto_dict = course_news_create_dto_instance.to_dict()
# create an instance of CourseNewsCreateDto from a dict
course_news_create_dto_from_dict = CourseNewsCreateDto.from_dict(course_news_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


