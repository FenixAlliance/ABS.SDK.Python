# WebsiteThemeDtoETag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_well_formed** | **bool** |  | [optional] 
**entity_type** | [**Type**](Type.md) |  | [optional] 
**is_any** | **bool** |  | [optional] 
**is_if_none_match** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.website_theme_dto_e_tag import WebsiteThemeDtoETag

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteThemeDtoETag from a JSON string
website_theme_dto_e_tag_instance = WebsiteThemeDtoETag.from_json(json)
# print the JSON string representation of the object
print(WebsiteThemeDtoETag.to_json())

# convert the object into a dict
website_theme_dto_e_tag_dict = website_theme_dto_e_tag_instance.to_dict()
# create an instance of WebsiteThemeDtoETag from a dict
website_theme_dto_e_tag_from_dict = WebsiteThemeDtoETag.from_dict(website_theme_dto_e_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


