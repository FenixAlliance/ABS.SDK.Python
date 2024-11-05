# ShipmentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ShipmentDto]**](ShipmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipment_dto_list_envelope import ShipmentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDtoListEnvelope from a JSON string
shipment_dto_list_envelope_instance = ShipmentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShipmentDtoListEnvelope.to_json())

# convert the object into a dict
shipment_dto_list_envelope_dict = shipment_dto_list_envelope_instance.to_dict()
# create an instance of ShipmentDtoListEnvelope from a dict
shipment_dto_list_envelope_from_dict = ShipmentDtoListEnvelope.from_dict(shipment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


