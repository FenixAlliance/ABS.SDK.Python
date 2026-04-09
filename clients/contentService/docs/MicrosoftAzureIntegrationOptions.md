# MicrosoftAzureIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**azure_app_insight** | [**AzureAppInsightIntegrationOptions**](AzureAppInsightIntegrationOptions.md) |  | [optional] 
**azure_storage** | [**AzureStorageIntegrationOptions**](AzureStorageIntegrationOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_azure_integration_options import MicrosoftAzureIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftAzureIntegrationOptions from a JSON string
microsoft_azure_integration_options_instance = MicrosoftAzureIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(MicrosoftAzureIntegrationOptions.to_json())

# convert the object into a dict
microsoft_azure_integration_options_dict = microsoft_azure_integration_options_instance.to_dict()
# create an instance of MicrosoftAzureIntegrationOptions from a dict
microsoft_azure_integration_options_from_dict = MicrosoftAzureIntegrationOptions.from_dict(microsoft_azure_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


