# LoanDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LoanDto]**](LoanDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.loan_dto_i_read_only_list_envelope import LoanDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LoanDtoIReadOnlyListEnvelope from a JSON string
loan_dto_i_read_only_list_envelope_instance = LoanDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LoanDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
loan_dto_i_read_only_list_envelope_dict = loan_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of LoanDtoIReadOnlyListEnvelope from a dict
loan_dto_i_read_only_list_envelope_from_dict = LoanDtoIReadOnlyListEnvelope.from_dict(loan_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


