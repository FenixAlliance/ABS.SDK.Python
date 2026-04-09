# BlogPostCategoryDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BlogPostCategoryDto**](BlogPostCategoryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.blog_post_category_dto_envelope import BlogPostCategoryDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BlogPostCategoryDtoEnvelope from a JSON string
blog_post_category_dto_envelope_instance = BlogPostCategoryDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BlogPostCategoryDtoEnvelope.to_json())

# convert the object into a dict
blog_post_category_dto_envelope_dict = blog_post_category_dto_envelope_instance.to_dict()
# create an instance of BlogPostCategoryDtoEnvelope from a dict
blog_post_category_dto_envelope_from_dict = BlogPostCategoryDtoEnvelope.from_dict(blog_post_category_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


