# EmployeeTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.employee_type_update_dto import EmployeeTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTypeUpdateDto from a JSON string
employee_type_update_dto_instance = EmployeeTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeTypeUpdateDto.to_json())

# convert the object into a dict
employee_type_update_dto_dict = employee_type_update_dto_instance.to_dict()
# create an instance of EmployeeTypeUpdateDto from a dict
employee_type_update_dto_from_dict = EmployeeTypeUpdateDto.from_dict(employee_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


