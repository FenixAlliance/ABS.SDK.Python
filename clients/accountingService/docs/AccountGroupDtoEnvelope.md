# AccountGroupDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AccountGroupDto**](AccountGroupDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_group_dto_envelope import AccountGroupDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AccountGroupDtoEnvelope from a JSON string
account_group_dto_envelope_instance = AccountGroupDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AccountGroupDtoEnvelope.to_json())

# convert the object into a dict
account_group_dto_envelope_dict = account_group_dto_envelope_instance.to_dict()
# create an instance of AccountGroupDtoEnvelope from a dict
account_group_dto_envelope_from_dict = AccountGroupDtoEnvelope.from_dict(account_group_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


