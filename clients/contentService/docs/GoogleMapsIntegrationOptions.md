# GoogleMapsIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**api_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_maps_integration_options import GoogleMapsIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleMapsIntegrationOptions from a JSON string
google_maps_integration_options_instance = GoogleMapsIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(GoogleMapsIntegrationOptions.to_json())

# convert the object into a dict
google_maps_integration_options_dict = google_maps_integration_options_instance.to_dict()
# create an instance of GoogleMapsIntegrationOptions from a dict
google_maps_integration_options_from_dict = GoogleMapsIntegrationOptions.from_dict(google_maps_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


