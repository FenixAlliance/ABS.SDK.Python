# FenixAllianceIntegrationsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**icx** | [**InfinityComexIntegrationOptions**](InfinityComexIntegrationOptions.md) |  | [optional] 
**abs** | [**AllianceBusinessSuiteIntegrationOptions**](AllianceBusinessSuiteIntegrationOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.fenix_alliance_integrations_options import FenixAllianceIntegrationsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FenixAllianceIntegrationsOptions from a JSON string
fenix_alliance_integrations_options_instance = FenixAllianceIntegrationsOptions.from_json(json)
# print the JSON string representation of the object
print(FenixAllianceIntegrationsOptions.to_json())

# convert the object into a dict
fenix_alliance_integrations_options_dict = fenix_alliance_integrations_options_instance.to_dict()
# create an instance of FenixAllianceIntegrationsOptions from a dict
fenix_alliance_integrations_options_from_dict = FenixAllianceIntegrationsOptions.from_dict(fenix_alliance_integrations_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


