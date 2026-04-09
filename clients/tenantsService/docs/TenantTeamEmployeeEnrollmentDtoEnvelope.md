# TenantTeamEmployeeEnrollmentDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TenantTeamEmployeeEnrollmentDto**](TenantTeamEmployeeEnrollmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_employee_enrollment_dto_envelope import TenantTeamEmployeeEnrollmentDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamEmployeeEnrollmentDtoEnvelope from a JSON string
tenant_team_employee_enrollment_dto_envelope_instance = TenantTeamEmployeeEnrollmentDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantTeamEmployeeEnrollmentDtoEnvelope.to_json())

# convert the object into a dict
tenant_team_employee_enrollment_dto_envelope_dict = tenant_team_employee_enrollment_dto_envelope_instance.to_dict()
# create an instance of TenantTeamEmployeeEnrollmentDtoEnvelope from a dict
tenant_team_employee_enrollment_dto_envelope_from_dict = TenantTeamEmployeeEnrollmentDtoEnvelope.from_dict(tenant_team_employee_enrollment_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


