# ColorOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_skin** | **str** |  | [optional] 
**primary_color** | **str** |  | [optional] 
**secondary_color** | **str** |  | [optional] 
**color_scheme** | [**ColorScheme**](ColorScheme.md) |  | [optional] 

## Example

```python
from openapi_client.models.color_options import ColorOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ColorOptions from a JSON string
color_options_instance = ColorOptions.from_json(json)
# print the JSON string representation of the object
print(ColorOptions.to_json())

# convert the object into a dict
color_options_dict = color_options_instance.to_dict()
# create an instance of ColorOptions from a dict
color_options_from_dict = ColorOptions.from_dict(color_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


