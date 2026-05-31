# PayrollCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**payroll_period_id** | **str** |  | 

## Example

```python
from openapi_client.models.payroll_create_dto import PayrollCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollCreateDto from a JSON string
payroll_create_dto_instance = PayrollCreateDto.from_json(json)
# print the JSON string representation of the object
print(PayrollCreateDto.to_json())

# convert the object into a dict
payroll_create_dto_dict = payroll_create_dto_instance.to_dict()
# create an instance of PayrollCreateDto from a dict
payroll_create_dto_from_dict = PayrollCreateDto.from_dict(payroll_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


