# WebsiteThemeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.website_theme_dto import WebsiteThemeDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteThemeDto from a JSON string
website_theme_dto_instance = WebsiteThemeDto.from_json(json)
# print the JSON string representation of the object
print(WebsiteThemeDto.to_json())

# convert the object into a dict
website_theme_dto_dict = website_theme_dto_instance.to_dict()
# create an instance of WebsiteThemeDto from a dict
website_theme_dto_from_dict = WebsiteThemeDto.from_dict(website_theme_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


