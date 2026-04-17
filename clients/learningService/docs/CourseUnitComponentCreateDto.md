# CourseUnitComponentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**course_id** | **str** |  | 
**course_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_unit_component_create_dto import CourseUnitComponentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseUnitComponentCreateDto from a JSON string
course_unit_component_create_dto_instance = CourseUnitComponentCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseUnitComponentCreateDto.to_json())

# convert the object into a dict
course_unit_component_create_dto_dict = course_unit_component_create_dto_instance.to_dict()
# create an instance of CourseUnitComponentCreateDto from a dict
course_unit_component_create_dto_from_dict = CourseUnitComponentCreateDto.from_dict(course_unit_component_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


