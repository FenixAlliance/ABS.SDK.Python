# PaymentModeDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PaymentModeDto]**](PaymentModeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_mode_dto_i_read_only_list_envelope import PaymentModeDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentModeDtoIReadOnlyListEnvelope from a JSON string
payment_mode_dto_i_read_only_list_envelope_instance = PaymentModeDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentModeDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
payment_mode_dto_i_read_only_list_envelope_dict = payment_mode_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of PaymentModeDtoIReadOnlyListEnvelope from a dict
payment_mode_dto_i_read_only_list_envelope_from_dict = PaymentModeDtoIReadOnlyListEnvelope.from_dict(payment_mode_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


