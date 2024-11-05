# UserSettingsDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**UserSettingsDto**](UserSettingsDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_settings_dto_envelope import UserSettingsDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsDtoEnvelope from a JSON string
user_settings_dto_envelope_instance = UserSettingsDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserSettingsDtoEnvelope.to_json())

# convert the object into a dict
user_settings_dto_envelope_dict = user_settings_dto_envelope_instance.to_dict()
# create an instance of UserSettingsDtoEnvelope from a dict
user_settings_dto_envelope_from_dict = UserSettingsDtoEnvelope.from_dict(user_settings_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


