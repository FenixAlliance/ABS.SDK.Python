# StudioOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | **str** |  | [optional] 
**logo_dark** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**icon_dark** | **str** |  | [optional] 
**favicon** | **str** |  | [optional] 
**logo_mobile** | **str** |  | [optional] 
**logo_mobile_dark** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.studio_options import StudioOptions

# TODO update the JSON string below
json = "{}"
# create an instance of StudioOptions from a JSON string
studio_options_instance = StudioOptions.from_json(json)
# print the JSON string representation of the object
print(StudioOptions.to_json())

# convert the object into a dict
studio_options_dict = studio_options_instance.to_dict()
# create an instance of StudioOptions from a dict
studio_options_from_dict = StudioOptions.from_dict(studio_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


