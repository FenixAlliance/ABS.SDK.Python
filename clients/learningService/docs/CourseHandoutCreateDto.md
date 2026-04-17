# CourseHandoutCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**course_id** | **str** |  | 
**course_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_handout_create_dto import CourseHandoutCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseHandoutCreateDto from a JSON string
course_handout_create_dto_instance = CourseHandoutCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseHandoutCreateDto.to_json())

# convert the object into a dict
course_handout_create_dto_dict = course_handout_create_dto_instance.to_dict()
# create an instance of CourseHandoutCreateDto from a dict
course_handout_create_dto_from_dict = CourseHandoutCreateDto.from_dict(course_handout_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


