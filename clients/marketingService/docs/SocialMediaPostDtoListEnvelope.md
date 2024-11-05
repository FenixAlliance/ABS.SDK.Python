# SocialMediaPostDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SocialMediaPostDto]**](SocialMediaPostDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_media_post_dto_list_envelope import SocialMediaPostDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialMediaPostDtoListEnvelope from a JSON string
social_media_post_dto_list_envelope_instance = SocialMediaPostDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialMediaPostDtoListEnvelope.to_json())

# convert the object into a dict
social_media_post_dto_list_envelope_dict = social_media_post_dto_list_envelope_instance.to_dict()
# create an instance of SocialMediaPostDtoListEnvelope from a dict
social_media_post_dto_list_envelope_from_dict = SocialMediaPostDtoListEnvelope.from_dict(social_media_post_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


