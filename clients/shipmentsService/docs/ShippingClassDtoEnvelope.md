# ShippingClassDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ShippingClassDto**](ShippingClassDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_class_dto_envelope import ShippingClassDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingClassDtoEnvelope from a JSON string
shipping_class_dto_envelope_instance = ShippingClassDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShippingClassDtoEnvelope.to_json())

# convert the object into a dict
shipping_class_dto_envelope_dict = shipping_class_dto_envelope_instance.to_dict()
# create an instance of ShippingClassDtoEnvelope from a dict
shipping_class_dto_envelope_from_dict = ShippingClassDtoEnvelope.from_dict(shipping_class_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


