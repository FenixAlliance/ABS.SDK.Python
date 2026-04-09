# FooterOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_columns** | **int** |  | [optional] 
**enable_widgets** | **bool** |  | [optional] 
**enable_copyright_bar** | **bool** |  | [optional] 
**center_widgets_content** | **bool** |  | [optional] 
**center_copyright_content** | **bool** |  | [optional] 
**enable_vertical_widget_divider_line** | **bool** |  | [optional] 
**vertical_widget_divider_line_size** | **int** |  | [optional] 
**copyright_text** | **str** |  | [optional] 
**copyright_background_color** | **str** |  | [optional] 
**border_size** | **int** |  | [optional] 
**border_color** | **str** |  | [optional] 
**widget_divider_color** | **str** |  | [optional] 
**widget_divider** | **str** |  | [optional] 
**copyright_padding** | [**Padding**](Padding.md) |  | [optional] 
**widgets_area_padding** | [**Padding**](Padding.md) |  | [optional] 
**footer_area_padding** | [**Padding**](Padding.md) |  | [optional] 
**footer_background** | [**Background**](Background.md) |  | [optional] 
**copyright_background** | [**Background**](Background.md) |  | [optional] 
**headings_typography** | [**Typography**](Typography.md) |  | [optional] 
**widgets_typography** | [**Typography**](Typography.md) |  | [optional] 
**copyright_typography** | [**Typography**](Typography.md) |  | [optional] 

## Example

```python
from openapi_client.models.footer_options import FooterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FooterOptions from a JSON string
footer_options_instance = FooterOptions.from_json(json)
# print the JSON string representation of the object
print(FooterOptions.to_json())

# convert the object into a dict
footer_options_dict = footer_options_instance.to_dict()
# create an instance of FooterOptions from a dict
footer_options_from_dict = FooterOptions.from_dict(footer_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


