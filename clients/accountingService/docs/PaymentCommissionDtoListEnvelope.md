# PaymentCommissionDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PaymentCommissionDto]**](PaymentCommissionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_commission_dto_list_envelope import PaymentCommissionDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCommissionDtoListEnvelope from a JSON string
payment_commission_dto_list_envelope_instance = PaymentCommissionDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentCommissionDtoListEnvelope.to_json())

# convert the object into a dict
payment_commission_dto_list_envelope_dict = payment_commission_dto_list_envelope_instance.to_dict()
# create an instance of PaymentCommissionDtoListEnvelope from a dict
payment_commission_dto_list_envelope_from_dict = PaymentCommissionDtoListEnvelope.from_dict(payment_commission_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


