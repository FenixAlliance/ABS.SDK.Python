# CourseCategoryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**is_featured** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.course_category_update_dto import CourseCategoryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCategoryUpdateDto from a JSON string
course_category_update_dto_instance = CourseCategoryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCategoryUpdateDto.to_json())

# convert the object into a dict
course_category_update_dto_dict = course_category_update_dto_instance.to_dict()
# create an instance of CourseCategoryUpdateDto from a dict
course_category_update_dto_from_dict = CourseCategoryUpdateDto.from_dict(course_category_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


