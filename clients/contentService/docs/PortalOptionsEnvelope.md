# PortalOptionsEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PortalOptions**](PortalOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.portal_options_envelope import PortalOptionsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PortalOptionsEnvelope from a JSON string
portal_options_envelope_instance = PortalOptionsEnvelope.from_json(json)
# print the JSON string representation of the object
print(PortalOptionsEnvelope.to_json())

# convert the object into a dict
portal_options_envelope_dict = portal_options_envelope_instance.to_dict()
# create an instance of PortalOptionsEnvelope from a dict
portal_options_envelope_from_dict = PortalOptionsEnvelope.from_dict(portal_options_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


