# SocialPostCommentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**social_post_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_post_comment_update_dto import SocialPostCommentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostCommentUpdateDto from a JSON string
social_post_comment_update_dto_instance = SocialPostCommentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SocialPostCommentUpdateDto.to_json())

# convert the object into a dict
social_post_comment_update_dto_dict = social_post_comment_update_dto_instance.to_dict()
# create an instance of SocialPostCommentUpdateDto from a dict
social_post_comment_update_dto_from_dict = SocialPostCommentUpdateDto.from_dict(social_post_comment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


