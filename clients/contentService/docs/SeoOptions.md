# SeoOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**social_image** | **str** |  | [optional] 
**title_suffix** | **str** |  | [optional] 
**bing_verification_code** | **str** |  | [optional] 
**google_verification_code** | **str** |  | [optional] 
**pinterest_verification_code** | **str** |  | [optional] 
**creator** | [**Creator**](Creator.md) |  | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 
**same_as** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.seo_options import SeoOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SeoOptions from a JSON string
seo_options_instance = SeoOptions.from_json(json)
# print the JSON string representation of the object
print(SeoOptions.to_json())

# convert the object into a dict
seo_options_dict = seo_options_instance.to_dict()
# create an instance of SeoOptions from a dict
seo_options_from_dict = SeoOptions.from_dict(seo_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


