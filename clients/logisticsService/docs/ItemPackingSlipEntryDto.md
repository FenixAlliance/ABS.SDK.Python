# ItemPackingSlipEntryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**quantity** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**item_packing_slip_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_packing_slip_entry_dto import ItemPackingSlipEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPackingSlipEntryDto from a JSON string
item_packing_slip_entry_dto_instance = ItemPackingSlipEntryDto.from_json(json)
# print the JSON string representation of the object
print(ItemPackingSlipEntryDto.to_json())

# convert the object into a dict
item_packing_slip_entry_dto_dict = item_packing_slip_entry_dto_instance.to_dict()
# create an instance of ItemPackingSlipEntryDto from a dict
item_packing_slip_entry_dto_from_dict = ItemPackingSlipEntryDto.from_dict(item_packing_slip_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


