# ItemPackingSlipCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**instructions** | **str** |  | [optional] 
**delivery_note_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_packing_slip_create_dto import ItemPackingSlipCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPackingSlipCreateDto from a JSON string
item_packing_slip_create_dto_instance = ItemPackingSlipCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemPackingSlipCreateDto.to_json())

# convert the object into a dict
item_packing_slip_create_dto_dict = item_packing_slip_create_dto_instance.to_dict()
# create an instance of ItemPackingSlipCreateDto from a dict
item_packing_slip_create_dto_from_dict = ItemPackingSlipCreateDto.from_dict(item_packing_slip_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


