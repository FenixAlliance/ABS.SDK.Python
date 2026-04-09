# CourseUnitUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**course_content_group_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_unit_update_dto import CourseUnitUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseUnitUpdateDto from a JSON string
course_unit_update_dto_instance = CourseUnitUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseUnitUpdateDto.to_json())

# convert the object into a dict
course_unit_update_dto_dict = course_unit_update_dto_instance.to_dict()
# create an instance of CourseUnitUpdateDto from a dict
course_unit_update_dto_from_dict = CourseUnitUpdateDto.from_dict(course_unit_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


