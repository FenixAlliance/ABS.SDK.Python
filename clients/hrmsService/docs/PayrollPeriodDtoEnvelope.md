# PayrollPeriodDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PayrollPeriodDto**](PayrollPeriodDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payroll_period_dto_envelope import PayrollPeriodDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollPeriodDtoEnvelope from a JSON string
payroll_period_dto_envelope_instance = PayrollPeriodDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PayrollPeriodDtoEnvelope.to_json())

# convert the object into a dict
payroll_period_dto_envelope_dict = payroll_period_dto_envelope_instance.to_dict()
# create an instance of PayrollPeriodDtoEnvelope from a dict
payroll_period_dto_envelope_from_dict = PayrollPeriodDtoEnvelope.from_dict(payroll_period_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


