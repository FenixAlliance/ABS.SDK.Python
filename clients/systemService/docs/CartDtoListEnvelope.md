# CartDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CartDto]**](CartDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.cart_dto_list_envelope import CartDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CartDtoListEnvelope from a JSON string
cart_dto_list_envelope_instance = CartDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CartDtoListEnvelope.to_json())

# convert the object into a dict
cart_dto_list_envelope_dict = cart_dto_list_envelope_instance.to_dict()
# create an instance of CartDtoListEnvelope from a dict
cart_dto_list_envelope_from_dict = CartDtoListEnvelope.from_dict(cart_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


