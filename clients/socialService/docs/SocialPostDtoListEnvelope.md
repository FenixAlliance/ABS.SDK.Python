# SocialPostDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SocialPostDto]**](SocialPostDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_post_dto_list_envelope import SocialPostDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialPostDtoListEnvelope from a JSON string
social_post_dto_list_envelope_instance = SocialPostDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialPostDtoListEnvelope.to_json())

# convert the object into a dict
social_post_dto_list_envelope_dict = social_post_dto_list_envelope_instance.to_dict()
# create an instance of SocialPostDtoListEnvelope from a dict
social_post_dto_list_envelope_from_dict = SocialPostDtoListEnvelope.from_dict(social_post_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


