# WalletDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**WalletDto**](WalletDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.wallet_dto_envelope import WalletDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WalletDtoEnvelope from a JSON string
wallet_dto_envelope_instance = WalletDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(WalletDtoEnvelope.to_json())

# convert the object into a dict
wallet_dto_envelope_dict = wallet_dto_envelope_instance.to_dict()
# create an instance of WalletDtoEnvelope from a dict
wallet_dto_envelope_from_dict = WalletDtoEnvelope.from_dict(wallet_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


