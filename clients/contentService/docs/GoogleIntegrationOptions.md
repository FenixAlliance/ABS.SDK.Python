# GoogleIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**google_maps** | [**GoogleMapsIntegrationOptions**](GoogleMapsIntegrationOptions.md) |  | [optional] 
**google_merchant_center** | [**GoogleMerchantCenterIntegrationOptions**](GoogleMerchantCenterIntegrationOptions.md) |  | [optional] 
**google_tag_manager** | [**GoogleTagManagerIntegrationOptions**](GoogleTagManagerIntegrationOptions.md) |  | [optional] 
**google_recaptcha** | [**GoogleRecaptchaIntegrationOptions**](GoogleRecaptchaIntegrationOptions.md) |  | [optional] 
**google_analytics** | [**GoogleAnalytics**](GoogleAnalytics.md) |  | [optional] 
**google_my_business** | [**GoogleMyBusinessIntegrationOptions**](GoogleMyBusinessIntegrationOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.google_integration_options import GoogleIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleIntegrationOptions from a JSON string
google_integration_options_instance = GoogleIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(GoogleIntegrationOptions.to_json())

# convert the object into a dict
google_integration_options_dict = google_integration_options_instance.to_dict()
# create an instance of GoogleIntegrationOptions from a dict
google_integration_options_from_dict = GoogleIntegrationOptions.from_dict(google_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


