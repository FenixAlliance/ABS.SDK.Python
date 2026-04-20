# BlogPostCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**published** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**markup** | **str** |  | [optional] 
**featured_image_url** | **str** |  | [optional] 
**code_type** | **str** |  | [optional] 
**blog_post_category_id** | **str** |  | [optional] 
**web_template_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.blog_post_create_dto import BlogPostCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlogPostCreateDto from a JSON string
blog_post_create_dto_instance = BlogPostCreateDto.from_json(json)
# print the JSON string representation of the object
print(BlogPostCreateDto.to_json())

# convert the object into a dict
blog_post_create_dto_dict = blog_post_create_dto_instance.to_dict()
# create an instance of BlogPostCreateDto from a dict
blog_post_create_dto_from_dict = BlogPostCreateDto.from_dict(blog_post_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


