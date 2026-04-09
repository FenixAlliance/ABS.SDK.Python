# PaymentTermDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PaymentTermDto]**](PaymentTermDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_term_dto_i_read_only_list_envelope import PaymentTermDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTermDtoIReadOnlyListEnvelope from a JSON string
payment_term_dto_i_read_only_list_envelope_instance = PaymentTermDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaymentTermDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
payment_term_dto_i_read_only_list_envelope_dict = payment_term_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of PaymentTermDtoIReadOnlyListEnvelope from a dict
payment_term_dto_i_read_only_list_envelope_from_dict = PaymentTermDtoIReadOnlyListEnvelope.from_dict(payment_term_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


