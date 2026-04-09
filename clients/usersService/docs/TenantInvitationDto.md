# TenantInvitationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**revoked** | **bool** |  | [optional] 
**redeemed** | **bool** |  | [optional] 
**redeemed_timestamp** | **datetime** |  | [optional] 
**user_email** | **str** |  | [optional] 
**creator_enrollment_id** | **str** |  | [optional] 
**related_enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_invitation_dto import TenantInvitationDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantInvitationDto from a JSON string
tenant_invitation_dto_instance = TenantInvitationDto.from_json(json)
# print the JSON string representation of the object
print(TenantInvitationDto.to_json())

# convert the object into a dict
tenant_invitation_dto_dict = tenant_invitation_dto_instance.to_dict()
# create an instance of TenantInvitationDto from a dict
tenant_invitation_dto_from_dict = TenantInvitationDto.from_dict(tenant_invitation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


