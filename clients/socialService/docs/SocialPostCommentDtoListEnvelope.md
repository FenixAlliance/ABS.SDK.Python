# SocialPostCommentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SocialPostCommentDto]**](SocialPostCommentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_post_comment_dto_list_envelope import SocialPostCommentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostCommentDtoListEnvelope from a JSON string
social_post_comment_dto_list_envelope_instance = SocialPostCommentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialPostCommentDtoListEnvelope.to_json())

# convert the object into a dict
social_post_comment_dto_list_envelope_dict = social_post_comment_dto_list_envelope_instance.to_dict()
# create an instance of SocialPostCommentDtoListEnvelope from a dict
social_post_comment_dto_list_envelope_from_dict = SocialPostCommentDtoListEnvelope.from_dict(social_post_comment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


