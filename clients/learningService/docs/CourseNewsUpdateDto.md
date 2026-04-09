# CourseNewsUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_news_update_dto import CourseNewsUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseNewsUpdateDto from a JSON string
course_news_update_dto_instance = CourseNewsUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseNewsUpdateDto.to_json())

# convert the object into a dict
course_news_update_dto_dict = course_news_update_dto_instance.to_dict()
# create an instance of CourseNewsUpdateDto from a dict
course_news_update_dto_from_dict = CourseNewsUpdateDto.from_dict(course_news_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


