# AddressDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[AddressDto]**](AddressDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.address_dto_list_envelope import AddressDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AddressDtoListEnvelope from a JSON string
address_dto_list_envelope_instance = AddressDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AddressDtoListEnvelope.to_json())

# convert the object into a dict
address_dto_list_envelope_dict = address_dto_list_envelope_instance.to_dict()
# create an instance of AddressDtoListEnvelope from a dict
address_dto_list_envelope_from_dict = AddressDtoListEnvelope.from_dict(address_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


