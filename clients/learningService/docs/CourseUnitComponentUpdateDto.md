# CourseUnitComponentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_unit_component_update_dto import CourseUnitComponentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseUnitComponentUpdateDto from a JSON string
course_unit_component_update_dto_instance = CourseUnitComponentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseUnitComponentUpdateDto.to_json())

# convert the object into a dict
course_unit_component_update_dto_dict = course_unit_component_update_dto_instance.to_dict()
# create an instance of CourseUnitComponentUpdateDto from a dict
course_unit_component_update_dto_from_dict = CourseUnitComponentUpdateDto.from_dict(course_unit_component_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


