# SocialPostCommentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 
**parent_comment_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**social_feed_post_id** | **str** |  | [optional] 
**social_profile_name** | **str** |  | [optional] 
**social_profile_avatar_url** | **str** |  | [optional] 
**social_post_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_comment_dto import SocialPostCommentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostCommentDto from a JSON string
social_post_comment_dto_instance = SocialPostCommentDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostCommentDto.to_json())

# convert the object into a dict
social_post_comment_dto_dict = social_post_comment_dto_instance.to_dict()
# create an instance of SocialPostCommentDto from a dict
social_post_comment_dto_from_dict = SocialPostCommentDto.from_dict(social_post_comment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


