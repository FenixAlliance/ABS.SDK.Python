# WalletWithdrawRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**requested_withdraw_amount** | **float** |  | [optional] 
**requested_withdraw_amount_in_usd** | **float** |  | [optional] 
**wallet_withdraw_request_status** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**wallet_account_id** | **str** |  | [optional] 
**bank_account_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.wallet_withdraw_request_dto import WalletWithdrawRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of WalletWithdrawRequestDto from a JSON string
wallet_withdraw_request_dto_instance = WalletWithdrawRequestDto.from_json(json)
# print the JSON string representation of the object
print(WalletWithdrawRequestDto.to_json())

# convert the object into a dict
wallet_withdraw_request_dto_dict = wallet_withdraw_request_dto_instance.to_dict()
# create an instance of WalletWithdrawRequestDto from a dict
wallet_withdraw_request_dto_from_dict = WalletWithdrawRequestDto.from_dict(wallet_withdraw_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


