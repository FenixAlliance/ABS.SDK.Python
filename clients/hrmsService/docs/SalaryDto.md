# SalaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**employee_profile_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.salary_dto import SalaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryDto from a JSON string
salary_dto_instance = SalaryDto.from_json(json)
# print the JSON string representation of the object
print(SalaryDto.to_json())

# convert the object into a dict
salary_dto_dict = salary_dto_instance.to_dict()
# create an instance of SalaryDto from a dict
salary_dto_from_dict = SalaryDto.from_dict(salary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


