# EmployeeTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**EmployeeTypeDto**](EmployeeTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.employee_type_dto_envelope import EmployeeTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTypeDtoEnvelope from a JSON string
employee_type_dto_envelope_instance = EmployeeTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmployeeTypeDtoEnvelope.to_json())

# convert the object into a dict
employee_type_dto_envelope_dict = employee_type_dto_envelope_instance.to_dict()
# create an instance of EmployeeTypeDtoEnvelope from a dict
employee_type_dto_envelope_from_dict = EmployeeTypeDtoEnvelope.from_dict(employee_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


