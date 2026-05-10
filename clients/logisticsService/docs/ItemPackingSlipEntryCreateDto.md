# ItemPackingSlipEntryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**item_id** | **str** |  | 
**item_packing_slip_id** | **str** |  | 
**quantity** | **str** |  | 

## Example

```python
from openapi_client.models.item_packing_slip_entry_create_dto import ItemPackingSlipEntryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPackingSlipEntryCreateDto from a JSON string
item_packing_slip_entry_create_dto_instance = ItemPackingSlipEntryCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemPackingSlipEntryCreateDto.to_json())

# convert the object into a dict
item_packing_slip_entry_create_dto_dict = item_packing_slip_entry_create_dto_instance.to_dict()
# create an instance of ItemPackingSlipEntryCreateDto from a dict
item_packing_slip_entry_create_dto_from_dict = ItemPackingSlipEntryCreateDto.from_dict(item_packing_slip_entry_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


