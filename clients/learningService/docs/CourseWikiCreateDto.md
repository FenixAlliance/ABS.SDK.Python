# CourseWikiCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**course_id** | **str** |  | 
**course_unit_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_wiki_create_dto import CourseWikiCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseWikiCreateDto from a JSON string
course_wiki_create_dto_instance = CourseWikiCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseWikiCreateDto.to_json())

# convert the object into a dict
course_wiki_create_dto_dict = course_wiki_create_dto_instance.to_dict()
# create an instance of CourseWikiCreateDto from a dict
course_wiki_create_dto_from_dict = CourseWikiCreateDto.from_dict(course_wiki_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


