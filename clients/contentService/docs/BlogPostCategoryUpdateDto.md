# BlogPostCategoryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**seo_title** | **str** |  | [optional] 
**meta_description** | **str** |  | [optional] 
**cornerstone_content** | **bool** |  | [optional] 
**allow_serach_engines** | **bool** |  | [optional] 
**seo_key_phrases** | **str** |  | [optional] 
**canonical_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**web_portal_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.blog_post_category_update_dto import BlogPostCategoryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlogPostCategoryUpdateDto from a JSON string
blog_post_category_update_dto_instance = BlogPostCategoryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(BlogPostCategoryUpdateDto.to_json())

# convert the object into a dict
blog_post_category_update_dto_dict = blog_post_category_update_dto_instance.to_dict()
# create an instance of BlogPostCategoryUpdateDto from a dict
blog_post_category_update_dto_from_dict = BlogPostCategoryUpdateDto.from_dict(blog_post_category_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


