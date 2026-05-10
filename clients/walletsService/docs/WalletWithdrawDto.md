# WalletWithdrawDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**withdraw_status** | **str** |  | [optional] 
**wallet_account_id** | **str** |  | [optional] 
**wallet_withdraw_request_id** | **str** |  | [optional] 
**balance_before_withdraw** | **float** |  | [optional] 
**balance_after_withdraw** | **float** |  | [optional] 
**withdrawed_amount** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.wallet_withdraw_dto import WalletWithdrawDto

# TODO update the JSON string below
json = "{}"
# create an instance of WalletWithdrawDto from a JSON string
wallet_withdraw_dto_instance = WalletWithdrawDto.from_json(json)
# print the JSON string representation of the object
print(WalletWithdrawDto.to_json())

# convert the object into a dict
wallet_withdraw_dto_dict = wallet_withdraw_dto_instance.to_dict()
# create an instance of WalletWithdrawDto from a dict
wallet_withdraw_dto_from_dict = WalletWithdrawDto.from_dict(wallet_withdraw_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


