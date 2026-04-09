# BrandingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_lang** | **str** |  | [optional] 
**primary_color** | **str** |  | [optional] 
**secondary_color** | **str** |  | [optional] 
**header_logo** | [**Logo**](Logo.md) |  | [optional] 
**footer_logo** | [**Logo**](Logo.md) |  | [optional] 
**favicons** | [**Favicons**](Favicons.md) |  | [optional] 
**apple_icon** | [**AppleIcons**](AppleIcons.md) |  | [optional] 
**ms_app_tile** | [**MSAppTile**](MSAppTile.md) |  | [optional] 
**dashboard** | [**DashboardOptions**](DashboardOptions.md) |  | [optional] 
**studio** | [**StudioOptions**](StudioOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.branding_options import BrandingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingOptions from a JSON string
branding_options_instance = BrandingOptions.from_json(json)
# print the JSON string representation of the object
print(BrandingOptions.to_json())

# convert the object into a dict
branding_options_dict = branding_options_instance.to_dict()
# create an instance of BrandingOptions from a dict
branding_options_from_dict = BrandingOptions.from_dict(branding_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


