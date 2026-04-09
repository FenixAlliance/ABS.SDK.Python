# CourseHandoutUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_handout_update_dto import CourseHandoutUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseHandoutUpdateDto from a JSON string
course_handout_update_dto_instance = CourseHandoutUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseHandoutUpdateDto.to_json())

# convert the object into a dict
course_handout_update_dto_dict = course_handout_update_dto_instance.to_dict()
# create an instance of CourseHandoutUpdateDto from a dict
course_handout_update_dto_from_dict = CourseHandoutUpdateDto.from_dict(course_handout_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


