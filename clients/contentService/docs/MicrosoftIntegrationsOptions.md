# MicrosoftIntegrationsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**azure** | [**MicrosoftAzureIntegrationOptions**](MicrosoftAzureIntegrationOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_integrations_options import MicrosoftIntegrationsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftIntegrationsOptions from a JSON string
microsoft_integrations_options_instance = MicrosoftIntegrationsOptions.from_json(json)
# print the JSON string representation of the object
print(MicrosoftIntegrationsOptions.to_json())

# convert the object into a dict
microsoft_integrations_options_dict = microsoft_integrations_options_instance.to_dict()
# create an instance of MicrosoftIntegrationsOptions from a dict
microsoft_integrations_options_from_dict = MicrosoftIntegrationsOptions.from_dict(microsoft_integrations_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


