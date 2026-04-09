# SecurityRoleDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SecurityRoleDto**](SecurityRoleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.security_role_dto_envelope import SecurityRoleDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRoleDtoEnvelope from a JSON string
security_role_dto_envelope_instance = SecurityRoleDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SecurityRoleDtoEnvelope.to_json())

# convert the object into a dict
security_role_dto_envelope_dict = security_role_dto_envelope_instance.to_dict()
# create an instance of SecurityRoleDtoEnvelope from a dict
security_role_dto_envelope_from_dict = SecurityRoleDtoEnvelope.from_dict(security_role_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


