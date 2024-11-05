# EmployeeProfileDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**EmployeeProfileDto**](EmployeeProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.employee_profile_dto_envelope import EmployeeProfileDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeProfileDtoEnvelope from a JSON string
employee_profile_dto_envelope_instance = EmployeeProfileDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmployeeProfileDtoEnvelope.to_json())

# convert the object into a dict
employee_profile_dto_envelope_dict = employee_profile_dto_envelope_instance.to_dict()
# create an instance of EmployeeProfileDtoEnvelope from a dict
employee_profile_dto_envelope_from_dict = EmployeeProfileDtoEnvelope.from_dict(employee_profile_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


