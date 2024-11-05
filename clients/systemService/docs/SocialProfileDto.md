# SocialProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**cover** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**identity_id** | **str** |  | [optional] 
**follows_count** | **int** |  | [optional] 
**messages_count** | **int** |  | [optional] 
**followers_count** | **int** |  | [optional] 
**notifications_count** | **int** |  | [optional] 
**unread_notifications_count** | **int** |  | [optional] 
**unread_messages_count** | **int** |  | [optional] 
**type** | **int** |  | [optional] 
**social_feed_id** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**youtube_url** | **str** |  | [optional] 
**github_url** | **str** |  | [optional] 
**pinterest_url** | **str** |  | [optional] 
**dribble_url** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.social_profile_dto import SocialProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocialProfileDto from a JSON string
social_profile_dto_instance = SocialProfileDto.from_json(json)
# print the JSON string representation of the object
print(SocialProfileDto.to_json())

# convert the object into a dict
social_profile_dto_dict = social_profile_dto_instance.to_dict()
# create an instance of SocialProfileDto from a dict
social_profile_dto_from_dict = SocialProfileDto.from_dict(social_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


