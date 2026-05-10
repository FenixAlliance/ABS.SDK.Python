# ShippingMethodDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ShippingMethodDto**](ShippingMethodDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_method_dto_envelope import ShippingMethodDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingMethodDtoEnvelope from a JSON string
shipping_method_dto_envelope_instance = ShippingMethodDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShippingMethodDtoEnvelope.to_json())

# convert the object into a dict
shipping_method_dto_envelope_dict = shipping_method_dto_envelope_instance.to_dict()
# create an instance of ShippingMethodDtoEnvelope from a dict
shipping_method_dto_envelope_from_dict = ShippingMethodDtoEnvelope.from_dict(shipping_method_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


