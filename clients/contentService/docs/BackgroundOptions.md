# BackgroundOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_pattern_id** | **int** |  | [optional] 
**enable_background_pattern** | **bool** |  | [optional] 
**background_image_for_page** | **str** |  | [optional] 
**background_color_for_page** | **str** |  | [optional] 
**main_content_color** | **str** |  | [optional] 
**main_content_image_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.background_options import BackgroundOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundOptions from a JSON string
background_options_instance = BackgroundOptions.from_json(json)
# print the JSON string representation of the object
print(BackgroundOptions.to_json())

# convert the object into a dict
background_options_dict = background_options_instance.to_dict()
# create an instance of BackgroundOptions from a dict
background_options_from_dict = BackgroundOptions.from_dict(background_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


