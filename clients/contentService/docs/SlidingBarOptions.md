# SlidingBarOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** |  | [optional] 
**content_padding** | [**Padding**](Padding.md) |  | [optional] 
**content_alignment** | **str** |  | [optional] 
**columns_count** | **int** |  | [optional] 
**enable_sticky** | **bool** |  | [optional] 
**open_on_page_load** | **bool** |  | [optional] 
**enable_on_mobile** | **bool** |  | [optional] 
**enable_on_desktop** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.sliding_bar_options import SlidingBarOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SlidingBarOptions from a JSON string
sliding_bar_options_instance = SlidingBarOptions.from_json(json)
# print the JSON string representation of the object
print(SlidingBarOptions.to_json())

# convert the object into a dict
sliding_bar_options_dict = sliding_bar_options_instance.to_dict()
# create an instance of SlidingBarOptions from a dict
sliding_bar_options_from_dict = SlidingBarOptions.from_dict(sliding_bar_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


