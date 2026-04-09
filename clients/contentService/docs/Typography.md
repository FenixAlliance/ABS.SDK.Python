# Typography


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_size** | **str** |  | [optional] 
**link_color** | **str** |  | [optional] 
**font_color** | **str** |  | [optional] 
**font_family** | **str** |  | [optional] 
**letter_spacing** | **str** |  | [optional] 
**link_color_hover** | **str** |  | [optional] 
**backup_font_family** | **str** |  | [optional] 
**font_weight_and_style** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.typography import Typography

# TODO update the JSON string below
json = "{}"
# create an instance of Typography from a JSON string
typography_instance = Typography.from_json(json)
# print the JSON string representation of the object
print(Typography.to_json())

# convert the object into a dict
typography_dict = typography_instance.to_dict()
# create an instance of Typography from a dict
typography_from_dict = Typography.from_dict(typography_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


