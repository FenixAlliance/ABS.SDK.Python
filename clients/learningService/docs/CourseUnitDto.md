# CourseUnitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**content** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**course_section_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**course_handouts** | [**List[CourseHandoutDto]**](CourseHandoutDto.md) |  | [optional] 
**course_assignments** | [**List[CourseAssignmentDto]**](CourseAssignmentDto.md) |  | [optional] 
**course_components** | [**List[CourseUnitComponentDto]**](CourseUnitComponentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.course_unit_dto import CourseUnitDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseUnitDto from a JSON string
course_unit_dto_instance = CourseUnitDto.from_json(json)
# print the JSON string representation of the object
print(CourseUnitDto.to_json())

# convert the object into a dict
course_unit_dto_dict = course_unit_dto_instance.to_dict()
# create an instance of CourseUnitDto from a dict
course_unit_dto_from_dict = CourseUnitDto.from_dict(course_unit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


