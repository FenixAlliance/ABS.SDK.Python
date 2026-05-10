# ShippingClassDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ShippingClassDto]**](ShippingClassDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_class_dto_list_envelope import ShippingClassDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingClassDtoListEnvelope from a JSON string
shipping_class_dto_list_envelope_instance = ShippingClassDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShippingClassDtoListEnvelope.to_json())

# convert the object into a dict
shipping_class_dto_list_envelope_dict = shipping_class_dto_list_envelope_instance.to_dict()
# create an instance of ShippingClassDtoListEnvelope from a dict
shipping_class_dto_list_envelope_from_dict = ShippingClassDtoListEnvelope.from_dict(shipping_class_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


