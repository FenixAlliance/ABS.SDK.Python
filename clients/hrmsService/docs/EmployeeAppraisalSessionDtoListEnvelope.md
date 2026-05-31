# EmployeeAppraisalSessionDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[EmployeeAppraisalSessionDto]**](EmployeeAppraisalSessionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.employee_appraisal_session_dto_list_envelope import EmployeeAppraisalSessionDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeAppraisalSessionDtoListEnvelope from a JSON string
employee_appraisal_session_dto_list_envelope_instance = EmployeeAppraisalSessionDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmployeeAppraisalSessionDtoListEnvelope.to_json())

# convert the object into a dict
employee_appraisal_session_dto_list_envelope_dict = employee_appraisal_session_dto_list_envelope_instance.to_dict()
# create an instance of EmployeeAppraisalSessionDtoListEnvelope from a dict
employee_appraisal_session_dto_list_envelope_from_dict = EmployeeAppraisalSessionDtoListEnvelope.from_dict(employee_appraisal_session_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


