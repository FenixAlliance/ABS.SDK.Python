# PaymentCommissionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PaymentCommissionDto**](PaymentCommissionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_commission_dto_envelope import PaymentCommissionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCommissionDtoEnvelope from a JSON string
payment_commission_dto_envelope_instance = PaymentCommissionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentCommissionDtoEnvelope.to_json())

# convert the object into a dict
payment_commission_dto_envelope_dict = payment_commission_dto_envelope_instance.to_dict()
# create an instance of PaymentCommissionDtoEnvelope from a dict
payment_commission_dto_envelope_from_dict = PaymentCommissionDtoEnvelope.from_dict(payment_commission_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


