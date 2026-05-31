# PayrollPeriodCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 

## Example

```python
from openapi_client.models.payroll_period_create_dto import PayrollPeriodCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollPeriodCreateDto from a JSON string
payroll_period_create_dto_instance = PayrollPeriodCreateDto.from_json(json)
# print the JSON string representation of the object
print(PayrollPeriodCreateDto.to_json())

# convert the object into a dict
payroll_period_create_dto_dict = payroll_period_create_dto_instance.to_dict()
# create an instance of PayrollPeriodCreateDto from a dict
payroll_period_create_dto_from_dict = PayrollPeriodCreateDto.from_dict(payroll_period_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


