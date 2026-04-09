# CourseWikiUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_wiki_update_dto import CourseWikiUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseWikiUpdateDto from a JSON string
course_wiki_update_dto_instance = CourseWikiUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseWikiUpdateDto.to_json())

# convert the object into a dict
course_wiki_update_dto_dict = course_wiki_update_dto_instance.to_dict()
# create an instance of CourseWikiUpdateDto from a dict
course_wiki_update_dto_from_dict = CourseWikiUpdateDto.from_dict(course_wiki_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


