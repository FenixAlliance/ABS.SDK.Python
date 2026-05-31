# WebsiteThemeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.website_theme_create_dto import WebsiteThemeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteThemeCreateDto from a JSON string
website_theme_create_dto_instance = WebsiteThemeCreateDto.from_json(json)
# print the JSON string representation of the object
print(WebsiteThemeCreateDto.to_json())

# convert the object into a dict
website_theme_create_dto_dict = website_theme_create_dto_instance.to_dict()
# create an instance of WebsiteThemeCreateDto from a dict
website_theme_create_dto_from_dict = WebsiteThemeCreateDto.from_dict(website_theme_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


