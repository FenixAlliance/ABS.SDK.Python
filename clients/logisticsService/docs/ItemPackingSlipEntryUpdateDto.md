# ItemPackingSlipEntryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_packing_slip_entry_update_dto import ItemPackingSlipEntryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPackingSlipEntryUpdateDto from a JSON string
item_packing_slip_entry_update_dto_instance = ItemPackingSlipEntryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemPackingSlipEntryUpdateDto.to_json())

# convert the object into a dict
item_packing_slip_entry_update_dto_dict = item_packing_slip_entry_update_dto_instance.to_dict()
# create an instance of ItemPackingSlipEntryUpdateDto from a dict
item_packing_slip_entry_update_dto_from_dict = ItemPackingSlipEntryUpdateDto.from_dict(item_packing_slip_entry_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


