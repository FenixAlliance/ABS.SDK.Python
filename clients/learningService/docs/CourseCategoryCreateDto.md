# CourseCategoryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**is_featured** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.course_category_create_dto import CourseCategoryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCategoryCreateDto from a JSON string
course_category_create_dto_instance = CourseCategoryCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCategoryCreateDto.to_json())

# convert the object into a dict
course_category_create_dto_dict = course_category_create_dto_instance.to_dict()
# create an instance of CourseCategoryCreateDto from a dict
course_category_create_dto_from_dict = CourseCategoryCreateDto.from_dict(course_category_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


