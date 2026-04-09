# SocialPostAttachmentDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SocialPostAttachmentDto**](SocialPostAttachmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_post_attachment_dto_envelope import SocialPostAttachmentDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostAttachmentDtoEnvelope from a JSON string
social_post_attachment_dto_envelope_instance = SocialPostAttachmentDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialPostAttachmentDtoEnvelope.to_json())

# convert the object into a dict
social_post_attachment_dto_envelope_dict = social_post_attachment_dto_envelope_instance.to_dict()
# create an instance of SocialPostAttachmentDtoEnvelope from a dict
social_post_attachment_dto_envelope_from_dict = SocialPostAttachmentDtoEnvelope.from_dict(social_post_attachment_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


