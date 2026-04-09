# SocialProfileDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SocialProfileDto**](SocialProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_profile_dto_envelope import SocialProfileDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialProfileDtoEnvelope from a JSON string
social_profile_dto_envelope_instance = SocialProfileDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialProfileDtoEnvelope.to_json())

# convert the object into a dict
social_profile_dto_envelope_dict = social_profile_dto_envelope_instance.to_dict()
# create an instance of SocialProfileDtoEnvelope from a dict
social_profile_dto_envelope_from_dict = SocialProfileDtoEnvelope.from_dict(social_profile_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


