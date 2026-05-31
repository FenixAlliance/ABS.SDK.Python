# EmployeeAppraisalSessionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**employee_profile_id** | **str** |  | 
**appraisal_workflow_id** | **str** |  | 
**appraisal_stage_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.employee_appraisal_session_create_dto import EmployeeAppraisalSessionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeAppraisalSessionCreateDto from a JSON string
employee_appraisal_session_create_dto_instance = EmployeeAppraisalSessionCreateDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeAppraisalSessionCreateDto.to_json())

# convert the object into a dict
employee_appraisal_session_create_dto_dict = employee_appraisal_session_create_dto_instance.to_dict()
# create an instance of EmployeeAppraisalSessionCreateDto from a dict
employee_appraisal_session_create_dto_from_dict = EmployeeAppraisalSessionCreateDto.from_dict(employee_appraisal_session_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


