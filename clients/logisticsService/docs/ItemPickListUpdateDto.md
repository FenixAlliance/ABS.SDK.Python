# ItemPickListUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_pick_list_update_dto import ItemPickListUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPickListUpdateDto from a JSON string
item_pick_list_update_dto_instance = ItemPickListUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemPickListUpdateDto.to_json())

# convert the object into a dict
item_pick_list_update_dto_dict = item_pick_list_update_dto_instance.to_dict()
# create an instance of ItemPickListUpdateDto from a dict
item_pick_list_update_dto_from_dict = ItemPickListUpdateDto.from_dict(item_pick_list_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


