# ResponsiveOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_responsive** | **bool** |  | [optional] 
**enable_mobile_zoom** | **bool** |  | [optional] 
**grid_responsive_breakpoint** | **bool** |  | [optional] 
**header_responsive_breakpoint** | **bool** |  | [optional] 
**content_responsive_breakpoint** | **bool** |  | [optional] 
**sidebar_responsive_breakpoint** | **bool** |  | [optional] 
**element_responsive_breakpoint_sm** | **int** |  | [optional] 
**element_responsive_breakpoint_md** | **int** |  | [optional] 
**element_responsive_breakpoint_lg** | **int** |  | [optional] 
**responsive_min_font_size_factor** | **float** |  | [optional] 
**typography_responsive_sensitivity** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.responsive_options import ResponsiveOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsiveOptions from a JSON string
responsive_options_instance = ResponsiveOptions.from_json(json)
# print the JSON string representation of the object
print(ResponsiveOptions.to_json())

# convert the object into a dict
responsive_options_dict = responsive_options_instance.to_dict()
# create an instance of ResponsiveOptions from a dict
responsive_options_from_dict = ResponsiveOptions.from_dict(responsive_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


