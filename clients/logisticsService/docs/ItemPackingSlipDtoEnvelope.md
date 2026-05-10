# ItemPackingSlipDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ItemPackingSlipDto**](ItemPackingSlipDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_packing_slip_dto_envelope import ItemPackingSlipDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPackingSlipDtoEnvelope from a JSON string
item_packing_slip_dto_envelope_instance = ItemPackingSlipDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemPackingSlipDtoEnvelope.to_json())

# convert the object into a dict
item_packing_slip_dto_envelope_dict = item_packing_slip_dto_envelope_instance.to_dict()
# create an instance of ItemPackingSlipDtoEnvelope from a dict
item_packing_slip_dto_envelope_from_dict = ItemPackingSlipDtoEnvelope.from_dict(item_packing_slip_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


