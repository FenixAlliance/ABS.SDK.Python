# GoogleMerchantCenterIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**merchant_user_email** | **str** |  | [optional] 
**json_credentials** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_merchant_center_integration_options import GoogleMerchantCenterIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleMerchantCenterIntegrationOptions from a JSON string
google_merchant_center_integration_options_instance = GoogleMerchantCenterIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(GoogleMerchantCenterIntegrationOptions.to_json())

# convert the object into a dict
google_merchant_center_integration_options_dict = google_merchant_center_integration_options_instance.to_dict()
# create an instance of GoogleMerchantCenterIntegrationOptions from a dict
google_merchant_center_integration_options_from_dict = GoogleMerchantCenterIntegrationOptions.from_dict(google_merchant_center_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


