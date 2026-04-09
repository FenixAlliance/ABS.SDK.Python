# FreeGeoIPIntegrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**api_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.free_geo_ip_integration_options import FreeGeoIPIntegrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FreeGeoIPIntegrationOptions from a JSON string
free_geo_ip_integration_options_instance = FreeGeoIPIntegrationOptions.from_json(json)
# print the JSON string representation of the object
print(FreeGeoIPIntegrationOptions.to_json())

# convert the object into a dict
free_geo_ip_integration_options_dict = free_geo_ip_integration_options_instance.to_dict()
# create an instance of FreeGeoIPIntegrationOptions from a dict
free_geo_ip_integration_options_from_dict = FreeGeoIPIntegrationOptions.from_dict(free_geo_ip_integration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


