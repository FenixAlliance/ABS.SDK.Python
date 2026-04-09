# BankAccountDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BankAccountDto**](BankAccountDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_account_dto_envelope import BankAccountDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDtoEnvelope from a JSON string
bank_account_dto_envelope_instance = BankAccountDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BankAccountDtoEnvelope.to_json())

# convert the object into a dict
bank_account_dto_envelope_dict = bank_account_dto_envelope_instance.to_dict()
# create an instance of BankAccountDtoEnvelope from a dict
bank_account_dto_envelope_from_dict = BankAccountDtoEnvelope.from_dict(bank_account_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


