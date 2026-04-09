# SocialFeedPostDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SocialFeedPostDto**](SocialFeedPostDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_feed_post_dto_envelope import SocialFeedPostDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialFeedPostDtoEnvelope from a JSON string
social_feed_post_dto_envelope_instance = SocialFeedPostDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialFeedPostDtoEnvelope.to_json())

# convert the object into a dict
social_feed_post_dto_envelope_dict = social_feed_post_dto_envelope_instance.to_dict()
# create an instance of SocialFeedPostDtoEnvelope from a dict
social_feed_post_dto_envelope_from_dict = SocialFeedPostDtoEnvelope.from_dict(social_feed_post_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


