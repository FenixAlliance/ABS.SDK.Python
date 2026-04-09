# GoogleRecaptchaIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**site** | **str** |  | [optional] 
**site_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_recaptcha_integration_options import GoogleRecaptchaIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleRecaptchaIntegrationOptions from a JSON string
google_recaptcha_integration_options_instance = GoogleRecaptchaIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(GoogleRecaptchaIntegrationOptions.to_json())

# convert the object into a dict
google_recaptcha_integration_options_dict = google_recaptcha_integration_options_instance.to_dict()
# create an instance of GoogleRecaptchaIntegrationOptions from a dict
google_recaptcha_integration_options_from_dict = GoogleRecaptchaIntegrationOptions.from_dict(google_recaptcha_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


