# EmployeeAppraisalSessionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**EmployeeAppraisalSessionDto**](EmployeeAppraisalSessionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.employee_appraisal_session_dto_envelope import EmployeeAppraisalSessionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeAppraisalSessionDtoEnvelope from a JSON string
employee_appraisal_session_dto_envelope_instance = EmployeeAppraisalSessionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmployeeAppraisalSessionDtoEnvelope.to_json())

# convert the object into a dict
employee_appraisal_session_dto_envelope_dict = employee_appraisal_session_dto_envelope_instance.to_dict()
# create an instance of EmployeeAppraisalSessionDtoEnvelope from a dict
employee_appraisal_session_dto_envelope_from_dict = EmployeeAppraisalSessionDtoEnvelope.from_dict(employee_appraisal_session_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


