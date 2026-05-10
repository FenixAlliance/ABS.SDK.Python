# PaymentTokenDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PaymentTokenDto**](PaymentTokenDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_token_dto_envelope import PaymentTokenDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTokenDtoEnvelope from a JSON string
payment_token_dto_envelope_instance = PaymentTokenDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentTokenDtoEnvelope.to_json())

# convert the object into a dict
payment_token_dto_envelope_dict = payment_token_dto_envelope_instance.to_dict()
# create an instance of PaymentTokenDtoEnvelope from a dict
payment_token_dto_envelope_from_dict = PaymentTokenDtoEnvelope.from_dict(payment_token_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


