# ShippingZoneDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**everywhere** | **bool** |  | [optional] 
**postal_codes** | **str** |  | [optional] 
**country_codes** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_zone_dto import ShippingZoneDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingZoneDto from a JSON string
shipping_zone_dto_instance = ShippingZoneDto.from_json(json)
# print the JSON string representation of the object
print(ShippingZoneDto.to_json())

# convert the object into a dict
shipping_zone_dto_dict = shipping_zone_dto_instance.to_dict()
# create an instance of ShippingZoneDto from a dict
shipping_zone_dto_from_dict = ShippingZoneDto.from_dict(shipping_zone_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


