# EmployeeTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.employee_type_create_dto import EmployeeTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTypeCreateDto from a JSON string
employee_type_create_dto_instance = EmployeeTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeTypeCreateDto.to_json())

# convert the object into a dict
employee_type_create_dto_dict = employee_type_create_dto_instance.to_dict()
# create an instance of EmployeeTypeCreateDto from a dict
employee_type_create_dto_from_dict = EmployeeTypeCreateDto.from_dict(employee_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


