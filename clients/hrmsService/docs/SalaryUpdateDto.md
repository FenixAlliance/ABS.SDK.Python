# SalaryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**employee_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.salary_update_dto import SalaryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryUpdateDto from a JSON string
salary_update_dto_instance = SalaryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SalaryUpdateDto.to_json())

# convert the object into a dict
salary_update_dto_dict = salary_update_dto_instance.to_dict()
# create an instance of SalaryUpdateDto from a dict
salary_update_dto_from_dict = SalaryUpdateDto.from_dict(salary_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


