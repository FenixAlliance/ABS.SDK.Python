# WalletWithdrawRequestDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[WalletWithdrawRequestDto]**](WalletWithdrawRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.wallet_withdraw_request_dto_list_envelope import WalletWithdrawRequestDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WalletWithdrawRequestDtoListEnvelope from a JSON string
wallet_withdraw_request_dto_list_envelope_instance = WalletWithdrawRequestDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(WalletWithdrawRequestDtoListEnvelope.to_json())

# convert the object into a dict
wallet_withdraw_request_dto_list_envelope_dict = wallet_withdraw_request_dto_list_envelope_instance.to_dict()
# create an instance of WalletWithdrawRequestDtoListEnvelope from a dict
wallet_withdraw_request_dto_list_envelope_from_dict = WalletWithdrawRequestDtoListEnvelope.from_dict(wallet_withdraw_request_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


