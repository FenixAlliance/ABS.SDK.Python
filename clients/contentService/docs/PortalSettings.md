# PortalSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**scopes** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**home_page_id** | **str** |  | [optional] 
**blog_page_id** | **str** |  | [optional] 
**store_page_id** | **str** |  | [optional] 
**base_endpoint** | **str** |  | [optional] 
**store_route_prefix** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**auth_token** | **str** |  | [optional] 
**auth_token_type** | **str** |  | [optional] 
**auth_token_expiration** | **int** |  | [optional] 
**options** | [**PortalOptions**](PortalOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.portal_settings import PortalSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortalSettings from a JSON string
portal_settings_instance = PortalSettings.from_json(json)
# print the JSON string representation of the object
print(PortalSettings.to_json())

# convert the object into a dict
portal_settings_dict = portal_settings_instance.to_dict()
# create an instance of PortalSettings from a dict
portal_settings_from_dict = PortalSettings.from_dict(portal_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


