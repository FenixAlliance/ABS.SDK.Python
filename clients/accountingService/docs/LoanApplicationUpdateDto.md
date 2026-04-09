# LoanApplicationUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.loan_application_update_dto import LoanApplicationUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoanApplicationUpdateDto from a JSON string
loan_application_update_dto_instance = LoanApplicationUpdateDto.from_json(json)
# print the JSON string representation of the object
print(LoanApplicationUpdateDto.to_json())

# convert the object into a dict
loan_application_update_dto_dict = loan_application_update_dto_instance.to_dict()
# create an instance of LoanApplicationUpdateDto from a dict
loan_application_update_dto_from_dict = LoanApplicationUpdateDto.from_dict(loan_application_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


