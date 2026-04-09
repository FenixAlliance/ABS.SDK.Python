# CoursePageUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_page_update_dto import CoursePageUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CoursePageUpdateDto from a JSON string
course_page_update_dto_instance = CoursePageUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CoursePageUpdateDto.to_json())

# convert the object into a dict
course_page_update_dto_dict = course_page_update_dto_instance.to_dict()
# create an instance of CoursePageUpdateDto from a dict
course_page_update_dto_from_dict = CoursePageUpdateDto.from_dict(course_page_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


