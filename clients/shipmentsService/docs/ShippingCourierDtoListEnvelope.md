# ShippingCourierDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ShippingCourierDto]**](ShippingCourierDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_courier_dto_list_envelope import ShippingCourierDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCourierDtoListEnvelope from a JSON string
shipping_courier_dto_list_envelope_instance = ShippingCourierDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShippingCourierDtoListEnvelope.to_json())

# convert the object into a dict
shipping_courier_dto_list_envelope_dict = shipping_courier_dto_list_envelope_instance.to_dict()
# create an instance of ShippingCourierDtoListEnvelope from a dict
shipping_courier_dto_list_envelope_from_dict = ShippingCourierDtoListEnvelope.from_dict(shipping_courier_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


