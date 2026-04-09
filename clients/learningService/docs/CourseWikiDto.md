# CourseWikiDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_wiki_dto import CourseWikiDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseWikiDto from a JSON string
course_wiki_dto_instance = CourseWikiDto.from_json(json)
# print the JSON string representation of the object
print(CourseWikiDto.to_json())

# convert the object into a dict
course_wiki_dto_dict = course_wiki_dto_instance.to_dict()
# create an instance of CourseWikiDto from a dict
course_wiki_dto_from_dict = CourseWikiDto.from_dict(course_wiki_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


