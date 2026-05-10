# PaymentChargebackDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PaymentChargebackDto]**](PaymentChargebackDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_chargeback_dto_list_envelope import PaymentChargebackDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentChargebackDtoListEnvelope from a JSON string
payment_chargeback_dto_list_envelope_instance = PaymentChargebackDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentChargebackDtoListEnvelope.to_json())

# convert the object into a dict
payment_chargeback_dto_list_envelope_dict = payment_chargeback_dto_list_envelope_instance.to_dict()
# create an instance of PaymentChargebackDtoListEnvelope from a dict
payment_chargeback_dto_list_envelope_from_dict = PaymentChargebackDtoListEnvelope.from_dict(payment_chargeback_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


