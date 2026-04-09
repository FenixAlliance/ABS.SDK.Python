# MenuOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side_navigation_font_size** | **str** |  | [optional] 
**main_menu_dropdown_font_color** | **str** |  | [optional] 
**main_menu_font_hover_active_color** | **str** |  | [optional] 
**main_menu_dropdown_separator_color** | **str** |  | [optional] 
**main_menu_dropdown_background_hover_color** | **str** |  | [optional] 
**main_menu_dropdown_background_color** | **str** |  | [optional] 
**menu_highlight_label_radius** | **str** |  | [optional] 
**enable_main_menu_cart_icon** | **bool** |  | [optional] 
**enable_main_menu_drop_shadow** | **bool** |  | [optional] 
**enable_main_menu_search_icon** | **bool** |  | [optional] 
**enable_main_menu_dropdown_divider** | **bool** |  | [optional] 
**enable_main_menu_notifications_icon** | **bool** |  | [optional] 
**enable_main_menu_icon_circle_borders** | **bool** |  | [optional] 
**main_menu_dropdown_width** | **int** |  | [optional] 
**main_menu_dropdown_font_size** | **int** |  | [optional] 
**main_menu_dropdown_item_padding** | **int** |  | [optional] 
**main_menu_dropdown_top_border_size** | **int** |  | [optional] 
**main_menu_height** | **int** |  | [optional] 
**main_menu_item_padding** | **int** |  | [optional] 
**main_menu_highlight_bar_size** | **int** |  | [optional] 
**main_menu_item_padding_on_mobile** | **int** |  | [optional] 
**main_menu_highlight_background_color** | **int** |  | [optional] 
**main_menu_typography** | [**Typography**](Typography.md) |  | [optional] 
**menu_highlight_style** | **str** |  | [optional] 
**main_menu_search_layout** | **str** |  | [optional] 
**menu_dropdown_animation** | **str** |  | [optional] 
**menu_dropdown_indicator** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.menu_options import MenuOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MenuOptions from a JSON string
menu_options_instance = MenuOptions.from_json(json)
# print the JSON string representation of the object
print(MenuOptions.to_json())

# convert the object into a dict
menu_options_dict = menu_options_instance.to_dict()
# create an instance of MenuOptions from a dict
menu_options_from_dict = MenuOptions.from_dict(menu_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


