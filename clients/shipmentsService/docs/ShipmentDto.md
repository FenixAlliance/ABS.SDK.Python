# ShipmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**tracking_code** | **str** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**shipment_timestamp** | **datetime** |  | [optional] 
**delivery_timestamp** | **datetime** |  | [optional] 
**expected_shipping_date** | **datetime** |  | [optional] 
**expected_delivery_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.shipment_dto import ShipmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDto from a JSON string
shipment_dto_instance = ShipmentDto.from_json(json)
# print the JSON string representation of the object
print(ShipmentDto.to_json())

# convert the object into a dict
shipment_dto_dict = shipment_dto_instance.to_dict()
# create an instance of ShipmentDto from a dict
shipment_dto_from_dict = ShipmentDto.from_dict(shipment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


