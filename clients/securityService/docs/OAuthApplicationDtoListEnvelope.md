# OAuthApplicationDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[OAuthApplicationDto]**](OAuthApplicationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_application_dto_list_envelope import OAuthApplicationDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplicationDtoListEnvelope from a JSON string
o_auth_application_dto_list_envelope_instance = OAuthApplicationDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(OAuthApplicationDtoListEnvelope.to_json())

# convert the object into a dict
o_auth_application_dto_list_envelope_dict = o_auth_application_dto_list_envelope_instance.to_dict()
# create an instance of OAuthApplicationDtoListEnvelope from a dict
o_auth_application_dto_list_envelope_from_dict = OAuthApplicationDtoListEnvelope.from_dict(o_auth_application_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


