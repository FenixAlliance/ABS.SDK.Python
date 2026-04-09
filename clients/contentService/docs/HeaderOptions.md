# HeaderOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_padding** | [**Padding**](Padding.md) |  | [optional] 
**header_background_image_url** | **str** |  | [optional] 
**header_background_color** | **str** |  | [optional] 
**header_border_color** | **str** |  | [optional] 
**enable_sticky_header** | **bool** |  | [optional] 
**enable_header_shadow** | **bool** |  | [optional] 
**enable_full_width_header** | **bool** |  | [optional] 
**header_layout** | **str** |  | [optional] 
**header_position** | **str** |  | [optional] 
**top_header_content_type2** | **str** |  | [optional] 
**top_header_content_type1** | **str** |  | [optional] 
**top_header_background_color** | **str** |  | [optional] 
**top_header_content1** | **str** |  | [optional] 
**top_header_content2** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.header_options import HeaderOptions

# TODO update the JSON string below
json = "{}"
# create an instance of HeaderOptions from a JSON string
header_options_instance = HeaderOptions.from_json(json)
# print the JSON string representation of the object
print(HeaderOptions.to_json())

# convert the object into a dict
header_options_dict = header_options_instance.to_dict()
# create an instance of HeaderOptions from a dict
header_options_from_dict = HeaderOptions.from_dict(header_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


