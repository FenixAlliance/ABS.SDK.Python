# TenantTeamContactEnrollmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_team_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_contact_enrollment_update_dto import TenantTeamContactEnrollmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamContactEnrollmentUpdateDto from a JSON string
tenant_team_contact_enrollment_update_dto_instance = TenantTeamContactEnrollmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamContactEnrollmentUpdateDto.to_json())

# convert the object into a dict
tenant_team_contact_enrollment_update_dto_dict = tenant_team_contact_enrollment_update_dto_instance.to_dict()
# create an instance of TenantTeamContactEnrollmentUpdateDto from a dict
tenant_team_contact_enrollment_update_dto_from_dict = TenantTeamContactEnrollmentUpdateDto.from_dict(tenant_team_contact_enrollment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


