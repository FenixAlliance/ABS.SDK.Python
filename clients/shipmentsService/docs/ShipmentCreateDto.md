# ShipmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tracking_code** | **str** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**expected_shipping_date** | **datetime** |  | [optional] 
**expected_delivery_date** | **datetime** |  | [optional] 
**shipping_terms** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipment_create_dto import ShipmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentCreateDto from a JSON string
shipment_create_dto_instance = ShipmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(ShipmentCreateDto.to_json())

# convert the object into a dict
shipment_create_dto_dict = shipment_create_dto_instance.to_dict()
# create an instance of ShipmentCreateDto from a dict
shipment_create_dto_from_dict = ShipmentCreateDto.from_dict(shipment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


