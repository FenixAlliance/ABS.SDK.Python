# MenuContextCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**category** | **str** |  | [optional] 
**component** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 
**studio_menu** | **bool** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**custom_js** | **str** |  | [optional] 
**custom_html** | **str** |  | [optional] 
**logged_in_only** | **str** |  | [optional] 
**background_image** | **str** |  | [optional] 
**web_portal_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.menu_context_create_dto import MenuContextCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MenuContextCreateDto from a JSON string
menu_context_create_dto_instance = MenuContextCreateDto.from_json(json)
# print the JSON string representation of the object
print(MenuContextCreateDto.to_json())

# convert the object into a dict
menu_context_create_dto_dict = menu_context_create_dto_instance.to_dict()
# create an instance of MenuContextCreateDto from a dict
menu_context_create_dto_from_dict = MenuContextCreateDto.from_dict(menu_context_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


