# CourseHandoutDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**course_id** | **str** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_handout_dto import CourseHandoutDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseHandoutDto from a JSON string
course_handout_dto_instance = CourseHandoutDto.from_json(json)
# print the JSON string representation of the object
print(CourseHandoutDto.to_json())

# convert the object into a dict
course_handout_dto_dict = course_handout_dto_instance.to_dict()
# create an instance of CourseHandoutDto from a dict
course_handout_dto_from_dict = CourseHandoutDto.from_dict(course_handout_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


