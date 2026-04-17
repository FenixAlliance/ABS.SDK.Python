# TenantInvitationCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**user_email** | **str** |  | 

## Example

```python
from openapi_client.models.tenant_invitation_create_dto import TenantInvitationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantInvitationCreateDto from a JSON string
tenant_invitation_create_dto_instance = TenantInvitationCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantInvitationCreateDto.to_json())

# convert the object into a dict
tenant_invitation_create_dto_dict = tenant_invitation_create_dto_instance.to_dict()
# create an instance of TenantInvitationCreateDto from a dict
tenant_invitation_create_dto_from_dict = TenantInvitationCreateDto.from_dict(tenant_invitation_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


