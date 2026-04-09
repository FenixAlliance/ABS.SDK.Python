# CourseSectionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**icon** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**hide_from_students** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_section_dto import CourseSectionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseSectionDto from a JSON string
course_section_dto_instance = CourseSectionDto.from_json(json)
# print the JSON string representation of the object
print(CourseSectionDto.to_json())

# convert the object into a dict
course_section_dto_dict = course_section_dto_instance.to_dict()
# create an instance of CourseSectionDto from a dict
course_section_dto_from_dict = CourseSectionDto.from_dict(course_section_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


