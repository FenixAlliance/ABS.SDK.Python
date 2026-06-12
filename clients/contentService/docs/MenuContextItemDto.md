# MenuContextItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**order** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**tooltip** | **str** |  | [optional] 
**parent_menu_context_item_id** | **str** |  | [optional] 
**menu_context_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.menu_context_item_dto import MenuContextItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of MenuContextItemDto from a JSON string
menu_context_item_dto_instance = MenuContextItemDto.from_json(json)
# print the JSON string representation of the object
print(MenuContextItemDto.to_json())

# convert the object into a dict
menu_context_item_dto_dict = menu_context_item_dto_instance.to_dict()
# create an instance of MenuContextItemDto from a dict
menu_context_item_dto_from_dict = MenuContextItemDto.from_dict(menu_context_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


