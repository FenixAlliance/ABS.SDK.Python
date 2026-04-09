# CourseCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_category_dto import CourseCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCategoryDto from a JSON string
course_category_dto_instance = CourseCategoryDto.from_json(json)
# print the JSON string representation of the object
print(CourseCategoryDto.to_json())

# convert the object into a dict
course_category_dto_dict = course_category_dto_instance.to_dict()
# create an instance of CourseCategoryDto from a dict
course_category_dto_from_dict = CourseCategoryDto.from_dict(course_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


