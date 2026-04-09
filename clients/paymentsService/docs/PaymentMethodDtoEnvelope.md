# PaymentMethodDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PaymentMethodDto**](PaymentMethodDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_dto_envelope import PaymentMethodDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodDtoEnvelope from a JSON string
payment_method_dto_envelope_instance = PaymentMethodDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodDtoEnvelope.to_json())

# convert the object into a dict
payment_method_dto_envelope_dict = payment_method_dto_envelope_instance.to_dict()
# create an instance of PaymentMethodDtoEnvelope from a dict
payment_method_dto_envelope_from_dict = PaymentMethodDtoEnvelope.from_dict(payment_method_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


