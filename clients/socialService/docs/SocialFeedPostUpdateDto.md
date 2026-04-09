# SocialFeedPostUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_feed_post_update_dto import SocialFeedPostUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialFeedPostUpdateDto from a JSON string
social_feed_post_update_dto_instance = SocialFeedPostUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SocialFeedPostUpdateDto.to_json())

# convert the object into a dict
social_feed_post_update_dto_dict = social_feed_post_update_dto_instance.to_dict()
# create an instance of SocialFeedPostUpdateDto from a dict
social_feed_post_update_dto_from_dict = SocialFeedPostUpdateDto.from_dict(social_feed_post_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


