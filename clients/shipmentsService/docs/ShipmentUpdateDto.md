# ShipmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_code** | **str** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**shipped** | **bool** |  | [optional] 
**delivered** | **bool** |  | [optional] 
**shipment_timestamp** | **datetime** |  | [optional] 
**delivery_timestamp** | **datetime** |  | [optional] 
**expected_shipping_date** | **datetime** |  | [optional] 
**expected_delivery_date** | **datetime** |  | [optional] 
**shipping_terms** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipment_update_dto import ShipmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentUpdateDto from a JSON string
shipment_update_dto_instance = ShipmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShipmentUpdateDto.to_json())

# convert the object into a dict
shipment_update_dto_dict = shipment_update_dto_instance.to_dict()
# create an instance of ShipmentUpdateDto from a dict
shipment_update_dto_from_dict = ShipmentUpdateDto.from_dict(shipment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


