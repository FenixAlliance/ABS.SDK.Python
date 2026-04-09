# LayoutOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**single_sidebar_width** | **str** |  | [optional] 
**single_sidebar_gutter** | **str** |  | [optional] 
**dial_sidebar_width1** | **str** |  | [optional] 
**dial_sidebar_width2** | **str** |  | [optional] 
**dial_sidebar_gutter** | **str** |  | [optional] 
**full_width_content_padding** | **str** |  | [optional] 
**page_content_padding_bottom** | **str** |  | [optional] 
**page_content_padding_top** | **str** |  | [optional] 
**site_width** | **str** |  | [optional] 
**layout** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.layout_options import LayoutOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LayoutOptions from a JSON string
layout_options_instance = LayoutOptions.from_json(json)
# print the JSON string representation of the object
print(LayoutOptions.to_json())

# convert the object into a dict
layout_options_dict = layout_options_instance.to_dict()
# create an instance of LayoutOptions from a dict
layout_options_from_dict = LayoutOptions.from_dict(layout_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


