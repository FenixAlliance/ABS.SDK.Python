# LoanApplicationCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.loan_application_create_dto import LoanApplicationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoanApplicationCreateDto from a JSON string
loan_application_create_dto_instance = LoanApplicationCreateDto.from_json(json)
# print the JSON string representation of the object
print(LoanApplicationCreateDto.to_json())

# convert the object into a dict
loan_application_create_dto_dict = loan_application_create_dto_instance.to_dict()
# create an instance of LoanApplicationCreateDto from a dict
loan_application_create_dto_from_dict = LoanApplicationCreateDto.from_dict(loan_application_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


