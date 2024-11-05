# PaymentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PaymentDto]**](PaymentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_dto_list_envelope import PaymentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDtoListEnvelope from a JSON string
payment_dto_list_envelope_instance = PaymentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentDtoListEnvelope.to_json())

# convert the object into a dict
payment_dto_list_envelope_dict = payment_dto_list_envelope_instance.to_dict()
# create an instance of PaymentDtoListEnvelope from a dict
payment_dto_list_envelope_from_dict = PaymentDtoListEnvelope.from_dict(payment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


