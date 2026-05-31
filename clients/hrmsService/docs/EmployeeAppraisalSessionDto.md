# EmployeeAppraisalSessionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**employee_profile_id** | **str** |  | [optional] 
**appraisal_workflow_id** | **str** |  | [optional] 
**appraisal_stage_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.employee_appraisal_session_dto import EmployeeAppraisalSessionDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeAppraisalSessionDto from a JSON string
employee_appraisal_session_dto_instance = EmployeeAppraisalSessionDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeAppraisalSessionDto.to_json())

# convert the object into a dict
employee_appraisal_session_dto_dict = employee_appraisal_session_dto_instance.to_dict()
# create an instance of EmployeeAppraisalSessionDto from a dict
employee_appraisal_session_dto_from_dict = EmployeeAppraisalSessionDto.from_dict(employee_appraisal_session_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


