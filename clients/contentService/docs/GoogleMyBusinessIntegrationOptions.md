# GoogleMyBusinessIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**client_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**auth_string** | **str** |  | [optional] 
**token_string** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**auth_provider_x509_cert_url** | **str** |  | [optional] 
**redirect_strings** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.google_my_business_integration_options import GoogleMyBusinessIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleMyBusinessIntegrationOptions from a JSON string
google_my_business_integration_options_instance = GoogleMyBusinessIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(GoogleMyBusinessIntegrationOptions.to_json())

# convert the object into a dict
google_my_business_integration_options_dict = google_my_business_integration_options_instance.to_dict()
# create an instance of GoogleMyBusinessIntegrationOptions from a dict
google_my_business_integration_options_from_dict = GoogleMyBusinessIntegrationOptions.from_dict(google_my_business_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


