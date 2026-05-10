# CartDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**CartDto**](CartDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.cart_dto_envelope import CartDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CartDtoEnvelope from a JSON string
cart_dto_envelope_instance = CartDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(CartDtoEnvelope.to_json())

# convert the object into a dict
cart_dto_envelope_dict = cart_dto_envelope_instance.to_dict()
# create an instance of CartDtoEnvelope from a dict
cart_dto_envelope_from_dict = CartDtoEnvelope.from_dict(cart_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


