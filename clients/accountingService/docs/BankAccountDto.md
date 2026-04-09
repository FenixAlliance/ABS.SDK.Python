# BankAccountDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**group** | **bool** |  | [optional] 
**frozen** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**balance** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**account_type_id** | **str** |  | [optional] 
**debits_balance** | **float** |  | [optional] 
**credits_balance** | **float** |  | [optional] 
**parent_account_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**children_accounts_count** | **int** |  | [optional] 
**account_category** | **str** |  | [optional] 
**balance_amount** | [**Money**](Money.md) |  | [optional] 
**credits_balance_amount** | [**Money**](Money.md) |  | [optional] 
**debits_balance_amount** | [**Money**](Money.md) |  | [optional] 
**iban** | **str** |  | [optional] 
**swift** | **str** |  | [optional] 
**branch_code** | **str** |  | [optional] 
**bank_account_number** | **str** |  | [optional] 
**qualified_name** | **str** |  | [optional] 
**bank_id** | **str** |  | [optional] 
**bank_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bank_account_dto import BankAccountDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDto from a JSON string
bank_account_dto_instance = BankAccountDto.from_json(json)
# print the JSON string representation of the object
print(BankAccountDto.to_json())

# convert the object into a dict
bank_account_dto_dict = bank_account_dto_instance.to_dict()
# create an instance of BankAccountDto from a dict
bank_account_dto_from_dict = BankAccountDto.from_dict(bank_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


