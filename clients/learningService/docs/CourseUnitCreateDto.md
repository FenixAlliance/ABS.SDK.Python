# CourseUnitCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**course_id** | **str** |  | 
**course_section_id** | **str** |  | 
**business_id** | **str** |  | 
**course_content_group_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_unit_create_dto import CourseUnitCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseUnitCreateDto from a JSON string
course_unit_create_dto_instance = CourseUnitCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseUnitCreateDto.to_json())

# convert the object into a dict
course_unit_create_dto_dict = course_unit_create_dto_instance.to_dict()
# create an instance of CourseUnitCreateDto from a dict
course_unit_create_dto_from_dict = CourseUnitCreateDto.from_dict(course_unit_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


