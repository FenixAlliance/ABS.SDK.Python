# SecurityRoleCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 
**tenant_id** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.security_role_create_dto import SecurityRoleCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRoleCreateDto from a JSON string
security_role_create_dto_instance = SecurityRoleCreateDto.from_json(json)
# print the JSON string representation of the object
print(SecurityRoleCreateDto.to_json())

# convert the object into a dict
security_role_create_dto_dict = security_role_create_dto_instance.to_dict()
# create an instance of SecurityRoleCreateDto from a dict
security_role_create_dto_from_dict = SecurityRoleCreateDto.from_dict(security_role_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


