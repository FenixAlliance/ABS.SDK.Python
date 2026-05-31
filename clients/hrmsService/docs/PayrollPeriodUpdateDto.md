# PayrollPeriodUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.payroll_period_update_dto import PayrollPeriodUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollPeriodUpdateDto from a JSON string
payroll_period_update_dto_instance = PayrollPeriodUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PayrollPeriodUpdateDto.to_json())

# convert the object into a dict
payroll_period_update_dto_dict = payroll_period_update_dto_instance.to_dict()
# create an instance of PayrollPeriodUpdateDto from a dict
payroll_period_update_dto_from_dict = PayrollPeriodUpdateDto.from_dict(payroll_period_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


