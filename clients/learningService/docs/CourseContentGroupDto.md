# CourseContentGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_content_group_dto import CourseContentGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseContentGroupDto from a JSON string
course_content_group_dto_instance = CourseContentGroupDto.from_json(json)
# print the JSON string representation of the object
print(CourseContentGroupDto.to_json())

# convert the object into a dict
course_content_group_dto_dict = course_content_group_dto_instance.to_dict()
# create an instance of CourseContentGroupDto from a dict
course_content_group_dto_from_dict = CourseContentGroupDto.from_dict(course_content_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


