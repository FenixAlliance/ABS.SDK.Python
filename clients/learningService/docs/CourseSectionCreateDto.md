# CourseSectionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**icon** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**course_id** | **str** |  | 
**release_date_time** | **datetime** |  | [optional] 
**hide_from_students** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.course_section_create_dto import CourseSectionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseSectionCreateDto from a JSON string
course_section_create_dto_instance = CourseSectionCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseSectionCreateDto.to_json())

# convert the object into a dict
course_section_create_dto_dict = course_section_create_dto_instance.to_dict()
# create an instance of CourseSectionCreateDto from a dict
course_section_create_dto_from_dict = CourseSectionCreateDto.from_dict(course_section_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


