# AccountDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AccountDto**](AccountDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_dto_envelope import AccountDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDtoEnvelope from a JSON string
account_dto_envelope_instance = AccountDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AccountDtoEnvelope.to_json())

# convert the object into a dict
account_dto_envelope_dict = account_dto_envelope_instance.to_dict()
# create an instance of AccountDtoEnvelope from a dict
account_dto_envelope_from_dict = AccountDtoEnvelope.from_dict(account_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


