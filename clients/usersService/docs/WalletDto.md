# WalletDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**balance** | **float** |  | [optional] 
**crypto_balance** | **float** |  | [optional] 
**test_mode** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**balance_in_usd** | **float** |  | [optional] 
**main_net_ether_balance** | **float** |  | [optional] 
**ethereum_address** | **str** |  | [optional] 
**ethereum_public_key** | **str** |  | [optional] 
**ethereum_private_key** | **str** |  | [optional] 
**rolling_reserve_percent** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.wallet_dto import WalletDto

# TODO update the JSON string below
json = "{}"
# create an instance of WalletDto from a JSON string
wallet_dto_instance = WalletDto.from_json(json)
# print the JSON string representation of the object
print(WalletDto.to_json())

# convert the object into a dict
wallet_dto_dict = wallet_dto_instance.to_dict()
# create an instance of WalletDto from a dict
wallet_dto_from_dict = WalletDto.from_dict(wallet_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


