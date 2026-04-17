# TenantTeamEmployeeEnrollmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_team_id** | **str** |  | [optional] 
**employee_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_employee_enrollment_update_dto import TenantTeamEmployeeEnrollmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamEmployeeEnrollmentUpdateDto from a JSON string
tenant_team_employee_enrollment_update_dto_instance = TenantTeamEmployeeEnrollmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamEmployeeEnrollmentUpdateDto.to_json())

# convert the object into a dict
tenant_team_employee_enrollment_update_dto_dict = tenant_team_employee_enrollment_update_dto_instance.to_dict()
# create an instance of TenantTeamEmployeeEnrollmentUpdateDto from a dict
tenant_team_employee_enrollment_update_dto_from_dict = TenantTeamEmployeeEnrollmentUpdateDto.from_dict(tenant_team_employee_enrollment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


