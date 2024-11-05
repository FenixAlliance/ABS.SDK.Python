# SecurityRoleUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.security_role_update_dto import SecurityRoleUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRoleUpdateDto from a JSON string
security_role_update_dto_instance = SecurityRoleUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SecurityRoleUpdateDto.to_json())

# convert the object into a dict
security_role_update_dto_dict = security_role_update_dto_instance.to_dict()
# create an instance of SecurityRoleUpdateDto from a dict
security_role_update_dto_from_dict = SecurityRoleUpdateDto.from_dict(security_role_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


