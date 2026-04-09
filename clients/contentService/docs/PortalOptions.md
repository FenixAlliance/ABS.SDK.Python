# PortalOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**portal_ui_engine** | **str** |  | [optional] 
**seo** | [**SeoOptions**](SeoOptions.md) |  | [optional] 
**store** | [**StoreOptions**](StoreOptions.md) |  | [optional] 
**theming** | [**ThemingOptions**](ThemingOptions.md) |  | [optional] 
**branding** | [**BrandingOptions**](BrandingOptions.md) |  | [optional] 
**social** | [**SocialMediaOptions**](SocialMediaOptions.md) |  | [optional] 
**privacy** | [**PrivacyOptions**](PrivacyOptions.md) |  | [optional] 
**blog** | [**BlogOptions**](BlogOptions.md) |  | [optional] 
**forums** | [**ForumOptions**](ForumOptions.md) |  | [optional] 
**footer** | [**FooterOptions**](FooterOptions.md) |  | [optional] 
**background** | [**BackgroundOptions**](BackgroundOptions.md) |  | [optional] 
**breadcrumbs** | [**BreadcrumbsOptions**](BreadcrumbsOptions.md) |  | [optional] 
**contact** | [**ContactOptions**](ContactOptions.md) |  | [optional] 
**color** | [**ColorOptions**](ColorOptions.md) |  | [optional] 
**dashboard** | [**DashboardOptions**](DashboardOptions.md) |  | [optional] 
**header** | [**HeaderOptions**](HeaderOptions.md) |  | [optional] 
**title_bar** | [**TitleBarOptions**](TitleBarOptions.md) |  | [optional] 
**typography** | [**TypographyOptions**](TypographyOptions.md) |  | [optional] 
**social_media** | [**SocialMediaOptions**](SocialMediaOptions.md) |  | [optional] 
**sliding_bar** | [**SlidingBarOptions**](SlidingBarOptions.md) |  | [optional] 
**slideshow** | **object** |  | [optional] 
**slider** | **object** |  | [optional] 
**sidebar** | **object** |  | [optional] 
**search** | **object** |  | [optional] 
**responsive** | [**ResponsiveOptions**](ResponsiveOptions.md) |  | [optional] 
**portfolio** | **object** |  | [optional] 
**performance** | **object** |  | [optional] 
**pagination** | **object** |  | [optional] 
**miscellaneous** | **object** |  | [optional] 
**menu** | [**MenuOptions**](MenuOptions.md) |  | [optional] 
**grid** | **object** |  | [optional] 
**mansory** | **object** |  | [optional] 
**lightbox** | **object** |  | [optional] 
**layout** | [**LayoutOptions**](LayoutOptions.md) |  | [optional] 
**code_fields** | **object** |  | [optional] 
**features** | **object** |  | [optional] 
**forms** | **object** |  | [optional] 
**integrations** | [**IntegrationsOptions**](IntegrationsOptions.md) |  | [optional] 
**emails** | [**EmailsOptions**](EmailsOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.portal_options import PortalOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PortalOptions from a JSON string
portal_options_instance = PortalOptions.from_json(json)
# print the JSON string representation of the object
print(PortalOptions.to_json())

# convert the object into a dict
portal_options_dict = portal_options_instance.to_dict()
# create an instance of PortalOptions from a dict
portal_options_from_dict = PortalOptions.from_dict(portal_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


