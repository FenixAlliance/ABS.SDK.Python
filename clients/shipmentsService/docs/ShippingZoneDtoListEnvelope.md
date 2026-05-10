# ShippingZoneDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ShippingZoneDto]**](ShippingZoneDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_zone_dto_list_envelope import ShippingZoneDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingZoneDtoListEnvelope from a JSON string
shipping_zone_dto_list_envelope_instance = ShippingZoneDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShippingZoneDtoListEnvelope.to_json())

# convert the object into a dict
shipping_zone_dto_list_envelope_dict = shipping_zone_dto_list_envelope_instance.to_dict()
# create an instance of ShippingZoneDtoListEnvelope from a dict
shipping_zone_dto_list_envelope_from_dict = ShippingZoneDtoListEnvelope.from_dict(shipping_zone_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


