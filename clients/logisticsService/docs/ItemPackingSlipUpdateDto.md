# ItemPackingSlipUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instructions** | **str** |  | [optional] 
**delivery_note_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_packing_slip_update_dto import ItemPackingSlipUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPackingSlipUpdateDto from a JSON string
item_packing_slip_update_dto_instance = ItemPackingSlipUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemPackingSlipUpdateDto.to_json())

# convert the object into a dict
item_packing_slip_update_dto_dict = item_packing_slip_update_dto_instance.to_dict()
# create an instance of ItemPackingSlipUpdateDto from a dict
item_packing_slip_update_dto_from_dict = ItemPackingSlipUpdateDto.from_dict(item_packing_slip_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


