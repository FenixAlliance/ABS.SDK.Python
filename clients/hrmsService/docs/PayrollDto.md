# PayrollDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**payroll_period_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payroll_dto import PayrollDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollDto from a JSON string
payroll_dto_instance = PayrollDto.from_json(json)
# print the JSON string representation of the object
print(PayrollDto.to_json())

# convert the object into a dict
payroll_dto_dict = payroll_dto_instance.to_dict()
# create an instance of PayrollDto from a dict
payroll_dto_from_dict = PayrollDto.from_dict(payroll_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


