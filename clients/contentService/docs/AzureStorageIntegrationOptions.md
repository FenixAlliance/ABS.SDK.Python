# AzureStorageIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**connection_string** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_storage_integration_options import AzureStorageIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AzureStorageIntegrationOptions from a JSON string
azure_storage_integration_options_instance = AzureStorageIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(AzureStorageIntegrationOptions.to_json())

# convert the object into a dict
azure_storage_integration_options_dict = azure_storage_integration_options_instance.to_dict()
# create an instance of AzureStorageIntegrationOptions from a dict
azure_storage_integration_options_from_dict = AzureStorageIntegrationOptions.from_dict(azure_storage_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


