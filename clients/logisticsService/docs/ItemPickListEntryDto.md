# ItemPickListEntryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**quantity** | **float** |  | [optional] 
**item_id** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**item_pick_list_id** | **str** |  | [optional] 
**order_item_record_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_pick_list_entry_dto import ItemPickListEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPickListEntryDto from a JSON string
item_pick_list_entry_dto_instance = ItemPickListEntryDto.from_json(json)
# print the JSON string representation of the object
print(ItemPickListEntryDto.to_json())

# convert the object into a dict
item_pick_list_entry_dto_dict = item_pick_list_entry_dto_instance.to_dict()
# create an instance of ItemPickListEntryDto from a dict
item_pick_list_entry_dto_from_dict = ItemPickListEntryDto.from_dict(item_pick_list_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


