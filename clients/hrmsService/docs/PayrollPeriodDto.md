# PayrollPeriodDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.payroll_period_dto import PayrollPeriodDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollPeriodDto from a JSON string
payroll_period_dto_instance = PayrollPeriodDto.from_json(json)
# print the JSON string representation of the object
print(PayrollPeriodDto.to_json())

# convert the object into a dict
payroll_period_dto_dict = payroll_period_dto_instance.to_dict()
# create an instance of PayrollPeriodDto from a dict
payroll_period_dto_from_dict = PayrollPeriodDto.from_dict(payroll_period_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


