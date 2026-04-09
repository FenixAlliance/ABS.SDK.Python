# SocialPostAttachmentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SocialPostAttachmentDto]**](SocialPostAttachmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_post_attachment_dto_list_envelope import SocialPostAttachmentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostAttachmentDtoListEnvelope from a JSON string
social_post_attachment_dto_list_envelope_instance = SocialPostAttachmentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialPostAttachmentDtoListEnvelope.to_json())

# convert the object into a dict
social_post_attachment_dto_list_envelope_dict = social_post_attachment_dto_list_envelope_instance.to_dict()
# create an instance of SocialPostAttachmentDtoListEnvelope from a dict
social_post_attachment_dto_list_envelope_from_dict = SocialPostAttachmentDtoListEnvelope.from_dict(social_post_attachment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


