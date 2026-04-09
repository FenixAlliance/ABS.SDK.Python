# SocialFeedPostDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**social_profile_name** | **str** |  | [optional] 
**social_profile_avatar_url** | **str** |  | [optional] 
**comments_count** | **int** |  | [optional] 
**reactions_count** | **int** |  | [optional] 
**social_feed_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_feed_post_dto import SocialFeedPostDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialFeedPostDto from a JSON string
social_feed_post_dto_instance = SocialFeedPostDto.from_json(json)
# print the JSON string representation of the object
print(SocialFeedPostDto.to_json())

# convert the object into a dict
social_feed_post_dto_dict = social_feed_post_dto_instance.to_dict()
# create an instance of SocialFeedPostDto from a dict
social_feed_post_dto_from_dict = SocialFeedPostDto.from_dict(social_feed_post_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


