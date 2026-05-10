# WalletWithdrawRequestCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**requested_withdraw_amount** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**bank_account_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.wallet_withdraw_request_create_dto import WalletWithdrawRequestCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WalletWithdrawRequestCreateDto from a JSON string
wallet_withdraw_request_create_dto_instance = WalletWithdrawRequestCreateDto.from_json(json)
# print the JSON string representation of the object
print(WalletWithdrawRequestCreateDto.to_json())

# convert the object into a dict
wallet_withdraw_request_create_dto_dict = wallet_withdraw_request_create_dto_instance.to_dict()
# create an instance of WalletWithdrawRequestCreateDto from a dict
wallet_withdraw_request_create_dto_from_dict = WalletWithdrawRequestCreateDto.from_dict(wallet_withdraw_request_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


