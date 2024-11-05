# SecurityRoleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_system_role** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.security_role_dto import SecurityRoleDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRoleDto from a JSON string
security_role_dto_instance = SecurityRoleDto.from_json(json)
# print the JSON string representation of the object
print(SecurityRoleDto.to_json())

# convert the object into a dict
security_role_dto_dict = security_role_dto_instance.to_dict()
# create an instance of SecurityRoleDto from a dict
security_role_dto_from_dict = SecurityRoleDto.from_dict(security_role_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


