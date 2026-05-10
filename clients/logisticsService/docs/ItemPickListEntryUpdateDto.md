# ItemPickListEntryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**order_item_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_pick_list_entry_update_dto import ItemPickListEntryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPickListEntryUpdateDto from a JSON string
item_pick_list_entry_update_dto_instance = ItemPickListEntryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemPickListEntryUpdateDto.to_json())

# convert the object into a dict
item_pick_list_entry_update_dto_dict = item_pick_list_entry_update_dto_instance.to_dict()
# create an instance of ItemPickListEntryUpdateDto from a dict
item_pick_list_entry_update_dto_from_dict = ItemPickListEntryUpdateDto.from_dict(item_pick_list_entry_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


