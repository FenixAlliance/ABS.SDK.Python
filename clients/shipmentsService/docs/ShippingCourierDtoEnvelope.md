# ShippingCourierDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ShippingCourierDto**](ShippingCourierDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_courier_dto_envelope import ShippingCourierDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCourierDtoEnvelope from a JSON string
shipping_courier_dto_envelope_instance = ShippingCourierDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShippingCourierDtoEnvelope.to_json())

# convert the object into a dict
shipping_courier_dto_envelope_dict = shipping_courier_dto_envelope_instance.to_dict()
# create an instance of ShippingCourierDtoEnvelope from a dict
shipping_courier_dto_envelope_from_dict = ShippingCourierDtoEnvelope.from_dict(shipping_courier_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


