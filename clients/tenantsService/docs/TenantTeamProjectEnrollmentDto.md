# TenantTeamProjectEnrollmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**team_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_project_enrollment_dto import TenantTeamProjectEnrollmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamProjectEnrollmentDto from a JSON string
tenant_team_project_enrollment_dto_instance = TenantTeamProjectEnrollmentDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamProjectEnrollmentDto.to_json())

# convert the object into a dict
tenant_team_project_enrollment_dto_dict = tenant_team_project_enrollment_dto_instance.to_dict()
# create an instance of TenantTeamProjectEnrollmentDto from a dict
tenant_team_project_enrollment_dto_from_dict = TenantTeamProjectEnrollmentDto.from_dict(tenant_team_project_enrollment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


