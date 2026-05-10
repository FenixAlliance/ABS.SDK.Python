# CourseContentGroupUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_content_group_update_dto import CourseContentGroupUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseContentGroupUpdateDto from a JSON string
course_content_group_update_dto_instance = CourseContentGroupUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseContentGroupUpdateDto.to_json())

# convert the object into a dict
course_content_group_update_dto_dict = course_content_group_update_dto_instance.to_dict()
# create an instance of CourseContentGroupUpdateDto from a dict
course_content_group_update_dto_from_dict = CourseContentGroupUpdateDto.from_dict(course_content_group_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


