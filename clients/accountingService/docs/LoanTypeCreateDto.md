# LoanTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.loan_type_create_dto import LoanTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoanTypeCreateDto from a JSON string
loan_type_create_dto_instance = LoanTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(LoanTypeCreateDto.to_json())

# convert the object into a dict
loan_type_create_dto_dict = loan_type_create_dto_instance.to_dict()
# create an instance of LoanTypeCreateDto from a dict
loan_type_create_dto_from_dict = LoanTypeCreateDto.from_dict(loan_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


