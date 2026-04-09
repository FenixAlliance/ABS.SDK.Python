# ThemingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dark_styling** | **bool** |  | [optional] 
**theme_name** | **str** |  | [optional] 
**default_layout** | **str** |  | [optional] 
**theme_assembly** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.theming_options import ThemingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ThemingOptions from a JSON string
theming_options_instance = ThemingOptions.from_json(json)
# print the JSON string representation of the object
print(ThemingOptions.to_json())

# convert the object into a dict
theming_options_dict = theming_options_instance.to_dict()
# create an instance of ThemingOptions from a dict
theming_options_from_dict = ThemingOptions.from_dict(theming_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


