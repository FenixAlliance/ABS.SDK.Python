# EmployeeAppraisalSessionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_profile_id** | **str** |  | [optional] 
**appraisal_workflow_id** | **str** |  | [optional] 
**appraisal_stage_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.employee_appraisal_session_update_dto import EmployeeAppraisalSessionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeAppraisalSessionUpdateDto from a JSON string
employee_appraisal_session_update_dto_instance = EmployeeAppraisalSessionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeAppraisalSessionUpdateDto.to_json())

# convert the object into a dict
employee_appraisal_session_update_dto_dict = employee_appraisal_session_update_dto_instance.to_dict()
# create an instance of EmployeeAppraisalSessionUpdateDto from a dict
employee_appraisal_session_update_dto_from_dict = EmployeeAppraisalSessionUpdateDto.from_dict(employee_appraisal_session_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


