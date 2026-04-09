# SocialGroupDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SocialGroupDto]**](SocialGroupDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.social_group_dto_list_envelope import SocialGroupDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SocialGroupDtoListEnvelope from a JSON string
social_group_dto_list_envelope_instance = SocialGroupDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SocialGroupDtoListEnvelope.to_json())

# convert the object into a dict
social_group_dto_list_envelope_dict = social_group_dto_list_envelope_instance.to_dict()
# create an instance of SocialGroupDtoListEnvelope from a dict
social_group_dto_list_envelope_from_dict = SocialGroupDtoListEnvelope.from_dict(social_group_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


