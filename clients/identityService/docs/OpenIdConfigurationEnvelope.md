# OpenIdConfigurationEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**OpenIdConfiguration**](OpenIdConfiguration.md) |  | [optional] 

## Example

```python
from openapi_client.models.open_id_configuration_envelope import OpenIdConfigurationEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConfigurationEnvelope from a JSON string
open_id_configuration_envelope_instance = OpenIdConfigurationEnvelope.from_json(json)
# print the JSON string representation of the object
print(OpenIdConfigurationEnvelope.to_json())

# convert the object into a dict
open_id_configuration_envelope_dict = open_id_configuration_envelope_instance.to_dict()
# create an instance of OpenIdConfigurationEnvelope from a dict
open_id_configuration_envelope_from_dict = OpenIdConfigurationEnvelope.from_dict(open_id_configuration_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


