# SecurityRoleDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SecurityRoleDto]**](SecurityRoleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.security_role_dto_list_envelope import SecurityRoleDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRoleDtoListEnvelope from a JSON string
security_role_dto_list_envelope_instance = SecurityRoleDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SecurityRoleDtoListEnvelope.to_json())

# convert the object into a dict
security_role_dto_list_envelope_dict = security_role_dto_list_envelope_instance.to_dict()
# create an instance of SecurityRoleDtoListEnvelope from a dict
security_role_dto_list_envelope_from_dict = SecurityRoleDtoListEnvelope.from_dict(security_role_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


