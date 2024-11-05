# SocialMediaPostDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SocialMediaPostDto**](SocialMediaPostDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_media_post_dto_envelope import SocialMediaPostDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialMediaPostDtoEnvelope from a JSON string
social_media_post_dto_envelope_instance = SocialMediaPostDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialMediaPostDtoEnvelope.to_json())

# convert the object into a dict
social_media_post_dto_envelope_dict = social_media_post_dto_envelope_instance.to_dict()
# create an instance of SocialMediaPostDtoEnvelope from a dict
social_media_post_dto_envelope_from_dict = SocialMediaPostDtoEnvelope.from_dict(social_media_post_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


