# LoanApplicationDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LoanApplicationDto]**](LoanApplicationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.loan_application_dto_i_read_only_list_envelope import LoanApplicationDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LoanApplicationDtoIReadOnlyListEnvelope from a JSON string
loan_application_dto_i_read_only_list_envelope_instance = LoanApplicationDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LoanApplicationDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
loan_application_dto_i_read_only_list_envelope_dict = loan_application_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of LoanApplicationDtoIReadOnlyListEnvelope from a dict
loan_application_dto_i_read_only_list_envelope_from_dict = LoanApplicationDtoIReadOnlyListEnvelope.from_dict(loan_application_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


