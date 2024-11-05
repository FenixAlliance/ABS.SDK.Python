# EmployeeProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.employee_profile_dto import EmployeeProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeProfileDto from a JSON string
employee_profile_dto_instance = EmployeeProfileDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeProfileDto.to_json())

# convert the object into a dict
employee_profile_dto_dict = employee_profile_dto_instance.to_dict()
# create an instance of EmployeeProfileDto from a dict
employee_profile_dto_from_dict = EmployeeProfileDto.from_dict(employee_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


