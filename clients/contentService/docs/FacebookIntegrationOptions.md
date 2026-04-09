# FacebookIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**pixel_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**app_secret** | **str** |  | [optional] 
**instagram_app_id** | **str** |  | [optional] 
**instagram_app_secret** | **str** |  | [optional] 
**marketing_api_token** | **str** |  | [optional] 
**marketing_api_token_sandbox** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.facebook_integration_options import FacebookIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookIntegrationOptions from a JSON string
facebook_integration_options_instance = FacebookIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(FacebookIntegrationOptions.to_json())

# convert the object into a dict
facebook_integration_options_dict = facebook_integration_options_instance.to_dict()
# create an instance of FacebookIntegrationOptions from a dict
facebook_integration_options_from_dict = FacebookIntegrationOptions.from_dict(facebook_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


