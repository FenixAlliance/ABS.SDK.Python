# EmployeeProfileCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.employee_profile_create_dto import EmployeeProfileCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeProfileCreateDto from a JSON string
employee_profile_create_dto_instance = EmployeeProfileCreateDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeProfileCreateDto.to_json())

# convert the object into a dict
employee_profile_create_dto_dict = employee_profile_create_dto_instance.to_dict()
# create an instance of EmployeeProfileCreateDto from a dict
employee_profile_create_dto_from_dict = EmployeeProfileCreateDto.from_dict(employee_profile_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


