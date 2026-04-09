# BlogPostCommentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**blog_post_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**owner_social_profile_id** | **str** |  | [optional] 
**social_post_id** | **str** |  | [optional] 
**parent_comment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.blog_post_comment_dto import BlogPostCommentDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlogPostCommentDto from a JSON string
blog_post_comment_dto_instance = BlogPostCommentDto.from_json(json)
# print the JSON string representation of the object
print(BlogPostCommentDto.to_json())

# convert the object into a dict
blog_post_comment_dto_dict = blog_post_comment_dto_instance.to_dict()
# create an instance of BlogPostCommentDto from a dict
blog_post_comment_dto_from_dict = BlogPostCommentDto.from_dict(blog_post_comment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


