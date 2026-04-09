# CourseUnitComponentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**course_id** | **str** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_unit_component_dto import CourseUnitComponentDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseUnitComponentDto from a JSON string
course_unit_component_dto_instance = CourseUnitComponentDto.from_json(json)
# print the JSON string representation of the object
print(CourseUnitComponentDto.to_json())

# convert the object into a dict
course_unit_component_dto_dict = course_unit_component_dto_instance.to_dict()
# create an instance of CourseUnitComponentDto from a dict
course_unit_component_dto_from_dict = CourseUnitComponentDto.from_dict(course_unit_component_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


