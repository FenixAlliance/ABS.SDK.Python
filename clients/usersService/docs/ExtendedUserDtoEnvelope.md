# ExtendedUserDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ExtendedUserDto**](ExtendedUserDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_user_dto_envelope import ExtendedUserDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedUserDtoEnvelope from a JSON string
extended_user_dto_envelope_instance = ExtendedUserDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExtendedUserDtoEnvelope.to_json())

# convert the object into a dict
extended_user_dto_envelope_dict = extended_user_dto_envelope_instance.to_dict()
# create an instance of ExtendedUserDtoEnvelope from a dict
extended_user_dto_envelope_from_dict = ExtendedUserDtoEnvelope.from_dict(extended_user_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


