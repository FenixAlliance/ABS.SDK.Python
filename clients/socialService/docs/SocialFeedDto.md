# SocialFeedDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**social_posts_count** | **int** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_feed_dto import SocialFeedDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialFeedDto from a JSON string
social_feed_dto_instance = SocialFeedDto.from_json(json)
# print the JSON string representation of the object
print(SocialFeedDto.to_json())

# convert the object into a dict
social_feed_dto_dict = social_feed_dto_instance.to_dict()
# create an instance of SocialFeedDto from a dict
social_feed_dto_from_dict = SocialFeedDto.from_dict(social_feed_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


