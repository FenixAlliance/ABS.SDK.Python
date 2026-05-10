# ShippingZoneDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ShippingZoneDto**](ShippingZoneDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_zone_dto_envelope import ShippingZoneDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingZoneDtoEnvelope from a JSON string
shipping_zone_dto_envelope_instance = ShippingZoneDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShippingZoneDtoEnvelope.to_json())

# convert the object into a dict
shipping_zone_dto_envelope_dict = shipping_zone_dto_envelope_instance.to_dict()
# create an instance of ShippingZoneDtoEnvelope from a dict
shipping_zone_dto_envelope_from_dict = ShippingZoneDtoEnvelope.from_dict(shipping_zone_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


