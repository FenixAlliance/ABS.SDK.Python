# BankTransactionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**bank_profile_id** | **str** |  | [optional] 
**bank_account_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bank_transaction_create_dto import BankTransactionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionCreateDto from a JSON string
bank_transaction_create_dto_instance = BankTransactionCreateDto.from_json(json)
# print the JSON string representation of the object
print(BankTransactionCreateDto.to_json())

# convert the object into a dict
bank_transaction_create_dto_dict = bank_transaction_create_dto_instance.to_dict()
# create an instance of BankTransactionCreateDto from a dict
bank_transaction_create_dto_from_dict = BankTransactionCreateDto.from_dict(bank_transaction_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


