# BankTransactionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BankTransactionDto**](BankTransactionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_transaction_dto_envelope import BankTransactionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionDtoEnvelope from a JSON string
bank_transaction_dto_envelope_instance = BankTransactionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BankTransactionDtoEnvelope.to_json())

# convert the object into a dict
bank_transaction_dto_envelope_dict = bank_transaction_dto_envelope_instance.to_dict()
# create an instance of BankTransactionDtoEnvelope from a dict
bank_transaction_dto_envelope_from_dict = BankTransactionDtoEnvelope.from_dict(bank_transaction_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


