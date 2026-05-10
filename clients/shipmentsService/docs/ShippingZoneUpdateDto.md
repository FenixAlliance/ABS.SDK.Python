# ShippingZoneUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**everywhere** | **bool** |  | [optional] 
**postal_codes** | **str** |  | [optional] 
**country_codes** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_zone_update_dto import ShippingZoneUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingZoneUpdateDto from a JSON string
shipping_zone_update_dto_instance = ShippingZoneUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ShippingZoneUpdateDto.to_json())

# convert the object into a dict
shipping_zone_update_dto_dict = shipping_zone_update_dto_instance.to_dict()
# create an instance of ShippingZoneUpdateDto from a dict
shipping_zone_update_dto_from_dict = ShippingZoneUpdateDto.from_dict(shipping_zone_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


