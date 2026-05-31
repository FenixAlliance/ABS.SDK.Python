# PayrollDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PayrollDto]**](PayrollDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.payroll_dto_list_envelope import PayrollDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollDtoListEnvelope from a JSON string
payroll_dto_list_envelope_instance = PayrollDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PayrollDtoListEnvelope.to_json())

# convert the object into a dict
payroll_dto_list_envelope_dict = payroll_dto_list_envelope_instance.to_dict()
# create an instance of PayrollDtoListEnvelope from a dict
payroll_dto_list_envelope_from_dict = PayrollDtoListEnvelope.from_dict(payroll_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


