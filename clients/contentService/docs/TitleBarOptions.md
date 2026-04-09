# TitleBarOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_fading_animations** | **bool** |  | [optional] 
**enable_page_title_bar_headings** | **bool** |  | [optional] 
**enable_full_width_page_title_bar** | **bool** |  | [optional] 
**enable_background_image_parallax** | **bool** |  | [optional] 
**enable_full_width_background_image** | **bool** |  | [optional] 
**background_image_url** | **str** |  | [optional] 
**retina_background_image_url** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**borders_color** | **str** |  | [optional] 
**heading_font_color** | **str** |  | [optional] 
**heading_font_size** | **str** |  | [optional] 
**heading_line_height** | **str** |  | [optional] 
**subheading_font_color** | **str** |  | [optional] 
**subheading_font_size** | **str** |  | [optional] 
**page_title_bar** | **str** |  | [optional] 
**page_title_bar_content** | **str** |  | [optional] 
**page_title_bar_text_alignment** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.title_bar_options import TitleBarOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TitleBarOptions from a JSON string
title_bar_options_instance = TitleBarOptions.from_json(json)
# print the JSON string representation of the object
print(TitleBarOptions.to_json())

# convert the object into a dict
title_bar_options_dict = title_bar_options_instance.to_dict()
# create an instance of TitleBarOptions from a dict
title_bar_options_from_dict = TitleBarOptions.from_dict(title_bar_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


