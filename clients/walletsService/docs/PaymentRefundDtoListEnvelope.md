# PaymentRefundDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PaymentRefundDto]**](PaymentRefundDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_refund_dto_list_envelope import PaymentRefundDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundDtoListEnvelope from a JSON string
payment_refund_dto_list_envelope_instance = PaymentRefundDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentRefundDtoListEnvelope.to_json())

# convert the object into a dict
payment_refund_dto_list_envelope_dict = payment_refund_dto_list_envelope_instance.to_dict()
# create an instance of PaymentRefundDtoListEnvelope from a dict
payment_refund_dto_list_envelope_from_dict = PaymentRefundDtoListEnvelope.from_dict(payment_refund_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


