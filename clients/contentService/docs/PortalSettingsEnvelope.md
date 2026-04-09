# PortalSettingsEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PortalSettings**](PortalSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.portal_settings_envelope import PortalSettingsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PortalSettingsEnvelope from a JSON string
portal_settings_envelope_instance = PortalSettingsEnvelope.from_json(json)
# print the JSON string representation of the object
print(PortalSettingsEnvelope.to_json())

# convert the object into a dict
portal_settings_envelope_dict = portal_settings_envelope_instance.to_dict()
# create an instance of PortalSettingsEnvelope from a dict
portal_settings_envelope_from_dict = PortalSettingsEnvelope.from_dict(portal_settings_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


