# SalaryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**amount** | **float** |  | 
**currency_id** | **str** |  | 
**employee_profile_id** | **str** |  | 

## Example

```python
from openapi_client.models.salary_create_dto import SalaryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryCreateDto from a JSON string
salary_create_dto_instance = SalaryCreateDto.from_json(json)
# print the JSON string representation of the object
print(SalaryCreateDto.to_json())

# convert the object into a dict
salary_create_dto_dict = salary_create_dto_instance.to_dict()
# create an instance of SalaryCreateDto from a dict
salary_create_dto_from_dict = SalaryCreateDto.from_dict(salary_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


