# ItemRestockEntryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**item_id** | **str** |  | 
**warehouse_id** | **str** |  | 
**item_restock_id** | **str** |  | 
**quantity** | **float** |  | [optional] 
**order_item_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_restock_entry_create_dto import ItemRestockEntryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRestockEntryCreateDto from a JSON string
item_restock_entry_create_dto_instance = ItemRestockEntryCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemRestockEntryCreateDto.to_json())

# convert the object into a dict
item_restock_entry_create_dto_dict = item_restock_entry_create_dto_instance.to_dict()
# create an instance of ItemRestockEntryCreateDto from a dict
item_restock_entry_create_dto_from_dict = ItemRestockEntryCreateDto.from_dict(item_restock_entry_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


