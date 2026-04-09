# BreadcrumbsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_breadcrumbs_on_mobile_devices** | **bool** |  | [optional] 
**enable_categories_on_breadcrumbs** | **bool** |  | [optional] 
**enable_post_types_on_breadcrumbs** | **bool** |  | [optional] 
**breadcrumbs_prefix** | **str** |  | [optional] 
**breadcrumbs_font_size** | **str** |  | [optional] 
**breadcrumbs_separator** | **str** |  | [optional] 
**breadcrumbs_font_color** | **str** |  | [optional] 
**breadcrumbs_font_color_hover** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.breadcrumbs_options import BreadcrumbsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BreadcrumbsOptions from a JSON string
breadcrumbs_options_instance = BreadcrumbsOptions.from_json(json)
# print the JSON string representation of the object
print(BreadcrumbsOptions.to_json())

# convert the object into a dict
breadcrumbs_options_dict = breadcrumbs_options_instance.to_dict()
# create an instance of BreadcrumbsOptions from a dict
breadcrumbs_options_from_dict = BreadcrumbsOptions.from_dict(breadcrumbs_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


