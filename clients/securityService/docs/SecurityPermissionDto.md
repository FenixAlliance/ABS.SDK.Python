# SecurityPermissionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_system_permission** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.security_permission_dto import SecurityPermissionDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPermissionDto from a JSON string
security_permission_dto_instance = SecurityPermissionDto.from_json(json)
# print the JSON string representation of the object
print(SecurityPermissionDto.to_json())

# convert the object into a dict
security_permission_dto_dict = security_permission_dto_instance.to_dict()
# create an instance of SecurityPermissionDto from a dict
security_permission_dto_from_dict = SecurityPermissionDto.from_dict(security_permission_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


