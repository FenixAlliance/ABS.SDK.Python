# ShippingLabelDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ShippingLabelDto**](ShippingLabelDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_label_dto_envelope import ShippingLabelDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingLabelDtoEnvelope from a JSON string
shipping_label_dto_envelope_instance = ShippingLabelDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShippingLabelDtoEnvelope.to_json())

# convert the object into a dict
shipping_label_dto_envelope_dict = shipping_label_dto_envelope_instance.to_dict()
# create an instance of ShippingLabelDtoEnvelope from a dict
shipping_label_dto_envelope_from_dict = ShippingLabelDtoEnvelope.from_dict(shipping_label_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


