# AccountTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AccountTypeDto**](AccountTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_type_dto_envelope import AccountTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTypeDtoEnvelope from a JSON string
account_type_dto_envelope_instance = AccountTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AccountTypeDtoEnvelope.to_json())

# convert the object into a dict
account_type_dto_envelope_dict = account_type_dto_envelope_instance.to_dict()
# create an instance of AccountTypeDtoEnvelope from a dict
account_type_dto_envelope_from_dict = AccountTypeDtoEnvelope.from_dict(account_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


