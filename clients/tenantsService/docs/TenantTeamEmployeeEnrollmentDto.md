# TenantTeamEmployeeEnrollmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**team_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**employee_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_employee_enrollment_dto import TenantTeamEmployeeEnrollmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamEmployeeEnrollmentDto from a JSON string
tenant_team_employee_enrollment_dto_instance = TenantTeamEmployeeEnrollmentDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamEmployeeEnrollmentDto.to_json())

# convert the object into a dict
tenant_team_employee_enrollment_dto_dict = tenant_team_employee_enrollment_dto_instance.to_dict()
# create an instance of TenantTeamEmployeeEnrollmentDto from a dict
tenant_team_employee_enrollment_dto_from_dict = TenantTeamEmployeeEnrollmentDto.from_dict(tenant_team_employee_enrollment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


