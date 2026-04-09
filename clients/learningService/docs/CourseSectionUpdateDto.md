# CourseSectionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**hide_from_students** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.course_section_update_dto import CourseSectionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseSectionUpdateDto from a JSON string
course_section_update_dto_instance = CourseSectionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseSectionUpdateDto.to_json())

# convert the object into a dict
course_section_update_dto_dict = course_section_update_dto_instance.to_dict()
# create an instance of CourseSectionUpdateDto from a dict
course_section_update_dto_from_dict = CourseSectionUpdateDto.from_dict(course_section_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


