# IntegrationsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**e_payco** | [**EPaycoIntegrationOptions**](EPaycoIntegrationOptions.md) |  | [optional] 
**google** | [**GoogleIntegrationOptions**](GoogleIntegrationOptions.md) |  | [optional] 
**facebook** | [**FacebookIntegrationOptions**](FacebookIntegrationOptions.md) |  | [optional] 
**sendgrid** | [**SendgridIntegrationsOptions**](SendgridIntegrationsOptions.md) |  | [optional] 
**free_geo_ip** | [**FreeGeoIPIntegrationOptions**](FreeGeoIPIntegrationOptions.md) |  | [optional] 
**microsoft** | [**MicrosoftIntegrationsOptions**](MicrosoftIntegrationsOptions.md) |  | [optional] 
**fenix_alliance** | [**FenixAllianceIntegrationsOptions**](FenixAllianceIntegrationsOptions.md) |  | [optional] 
**open_exchange_rates** | [**OpenExchangeRatesIntegrationsOptions**](OpenExchangeRatesIntegrationsOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.integrations_options import IntegrationsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationsOptions from a JSON string
integrations_options_instance = IntegrationsOptions.from_json(json)
# print the JSON string representation of the object
print(IntegrationsOptions.to_json())

# convert the object into a dict
integrations_options_dict = integrations_options_instance.to_dict()
# create an instance of IntegrationsOptions from a dict
integrations_options_from_dict = IntegrationsOptions.from_dict(integrations_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


