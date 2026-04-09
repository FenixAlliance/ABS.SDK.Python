# LoanApplicationDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**LoanApplicationDto**](LoanApplicationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.loan_application_dto_envelope import LoanApplicationDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LoanApplicationDtoEnvelope from a JSON string
loan_application_dto_envelope_instance = LoanApplicationDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(LoanApplicationDtoEnvelope.to_json())

# convert the object into a dict
loan_application_dto_envelope_dict = loan_application_dto_envelope_instance.to_dict()
# create an instance of LoanApplicationDtoEnvelope from a dict
loan_application_dto_envelope_from_dict = LoanApplicationDtoEnvelope.from_dict(loan_application_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


