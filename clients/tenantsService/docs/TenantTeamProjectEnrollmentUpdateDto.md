# TenantTeamProjectEnrollmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**business_team_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_project_enrollment_update_dto import TenantTeamProjectEnrollmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamProjectEnrollmentUpdateDto from a JSON string
tenant_team_project_enrollment_update_dto_instance = TenantTeamProjectEnrollmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamProjectEnrollmentUpdateDto.to_json())

# convert the object into a dict
tenant_team_project_enrollment_update_dto_dict = tenant_team_project_enrollment_update_dto_instance.to_dict()
# create an instance of TenantTeamProjectEnrollmentUpdateDto from a dict
tenant_team_project_enrollment_update_dto_from_dict = TenantTeamProjectEnrollmentUpdateDto.from_dict(tenant_team_project_enrollment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


