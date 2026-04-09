# PaymentModeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PaymentModeDto**](PaymentModeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_mode_dto_envelope import PaymentModeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentModeDtoEnvelope from a JSON string
payment_mode_dto_envelope_instance = PaymentModeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentModeDtoEnvelope.to_json())

# convert the object into a dict
payment_mode_dto_envelope_dict = payment_mode_dto_envelope_instance.to_dict()
# create an instance of PaymentModeDtoEnvelope from a dict
payment_mode_dto_envelope_from_dict = PaymentModeDtoEnvelope.from_dict(payment_mode_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


