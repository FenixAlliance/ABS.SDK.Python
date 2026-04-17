# BankAccountCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**group** | **bool** |  | [optional] 
**frozen** | **bool** |  | [optional] 
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**currency_id** | **str** |  | 
**account_type_id** | **str** |  | [optional] 
**parent_account_id** | **str** |  | [optional] 
**account_category** | **str** |  | 
**iban** | **str** |  | [optional] 
**swift** | **str** |  | [optional] 
**branch_code** | **str** |  | [optional] 
**bank_account_number** | **str** |  | [optional] 
**qualified_name** | **str** |  | [optional] 
**bank_id** | **str** |  | [optional] 
**bank_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bank_account_create_dto import BankAccountCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCreateDto from a JSON string
bank_account_create_dto_instance = BankAccountCreateDto.from_json(json)
# print the JSON string representation of the object
print(BankAccountCreateDto.to_json())

# convert the object into a dict
bank_account_create_dto_dict = bank_account_create_dto_instance.to_dict()
# create an instance of BankAccountCreateDto from a dict
bank_account_create_dto_from_dict = BankAccountCreateDto.from_dict(bank_account_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


