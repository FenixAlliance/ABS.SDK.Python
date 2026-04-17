# TenantTeamContactEnrollmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_team_id** | **str** |  | 
**contact_id** | **str** |  | 

## Example

```python
from openapi_client.models.tenant_team_contact_enrollment_create_dto import TenantTeamContactEnrollmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamContactEnrollmentCreateDto from a JSON string
tenant_team_contact_enrollment_create_dto_instance = TenantTeamContactEnrollmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamContactEnrollmentCreateDto.to_json())

# convert the object into a dict
tenant_team_contact_enrollment_create_dto_dict = tenant_team_contact_enrollment_create_dto_instance.to_dict()
# create an instance of TenantTeamContactEnrollmentCreateDto from a dict
tenant_team_contact_enrollment_create_dto_from_dict = TenantTeamContactEnrollmentCreateDto.from_dict(tenant_team_contact_enrollment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


