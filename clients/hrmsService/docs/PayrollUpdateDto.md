# PayrollUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_period_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payroll_update_dto import PayrollUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollUpdateDto from a JSON string
payroll_update_dto_instance = PayrollUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PayrollUpdateDto.to_json())

# convert the object into a dict
payroll_update_dto_dict = payroll_update_dto_instance.to_dict()
# create an instance of PayrollUpdateDto from a dict
payroll_update_dto_from_dict = PayrollUpdateDto.from_dict(payroll_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


