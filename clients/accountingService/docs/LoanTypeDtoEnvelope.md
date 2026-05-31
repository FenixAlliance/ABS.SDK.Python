# LoanTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**LoanTypeDto**](LoanTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.loan_type_dto_envelope import LoanTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LoanTypeDtoEnvelope from a JSON string
loan_type_dto_envelope_instance = LoanTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(LoanTypeDtoEnvelope.to_json())

# convert the object into a dict
loan_type_dto_envelope_dict = loan_type_dto_envelope_instance.to_dict()
# create an instance of LoanTypeDtoEnvelope from a dict
loan_type_dto_envelope_from_dict = LoanTypeDtoEnvelope.from_dict(loan_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


