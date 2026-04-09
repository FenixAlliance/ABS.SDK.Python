# SocialFeedPostCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**social_feed_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_feed_post_create_dto import SocialFeedPostCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialFeedPostCreateDto from a JSON string
social_feed_post_create_dto_instance = SocialFeedPostCreateDto.from_json(json)
# print the JSON string representation of the object
print(SocialFeedPostCreateDto.to_json())

# convert the object into a dict
social_feed_post_create_dto_dict = social_feed_post_create_dto_instance.to_dict()
# create an instance of SocialFeedPostCreateDto from a dict
social_feed_post_create_dto_from_dict = SocialFeedPostCreateDto.from_dict(social_feed_post_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


