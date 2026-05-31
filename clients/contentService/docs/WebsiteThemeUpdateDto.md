# WebsiteThemeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.website_theme_update_dto import WebsiteThemeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteThemeUpdateDto from a JSON string
website_theme_update_dto_instance = WebsiteThemeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(WebsiteThemeUpdateDto.to_json())

# convert the object into a dict
website_theme_update_dto_dict = website_theme_update_dto_instance.to_dict()
# create an instance of WebsiteThemeUpdateDto from a dict
website_theme_update_dto_from_dict = WebsiteThemeUpdateDto.from_dict(website_theme_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


