# PaymentTokenDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PaymentTokenDto]**](PaymentTokenDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_token_dto_list_envelope import PaymentTokenDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTokenDtoListEnvelope from a JSON string
payment_token_dto_list_envelope_instance = PaymentTokenDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentTokenDtoListEnvelope.to_json())

# convert the object into a dict
payment_token_dto_list_envelope_dict = payment_token_dto_list_envelope_instance.to_dict()
# create an instance of PaymentTokenDtoListEnvelope from a dict
payment_token_dto_list_envelope_from_dict = PaymentTokenDtoListEnvelope.from_dict(payment_token_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


