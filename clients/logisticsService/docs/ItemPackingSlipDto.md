# ItemPackingSlipDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**instructions** | **str** |  | [optional] 
**delivery_note_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_packing_slip_dto import ItemPackingSlipDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPackingSlipDto from a JSON string
item_packing_slip_dto_instance = ItemPackingSlipDto.from_json(json)
# print the JSON string representation of the object
print(ItemPackingSlipDto.to_json())

# convert the object into a dict
item_packing_slip_dto_dict = item_packing_slip_dto_instance.to_dict()
# create an instance of ItemPackingSlipDto from a dict
item_packing_slip_dto_from_dict = ItemPackingSlipDto.from_dict(item_packing_slip_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


