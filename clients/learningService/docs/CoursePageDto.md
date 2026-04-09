# CoursePageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_page_dto import CoursePageDto

# TODO update the JSON string below
json = "{}"
# create an instance of CoursePageDto from a JSON string
course_page_dto_instance = CoursePageDto.from_json(json)
# print the JSON string representation of the object
print(CoursePageDto.to_json())

# convert the object into a dict
course_page_dto_dict = course_page_dto_instance.to_dict()
# create an instance of CoursePageDto from a dict
course_page_dto_from_dict = CoursePageDto.from_dict(course_page_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


