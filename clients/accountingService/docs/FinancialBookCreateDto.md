# FinancialBookCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.financial_book_create_dto import FinancialBookCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialBookCreateDto from a JSON string
financial_book_create_dto_instance = FinancialBookCreateDto.from_json(json)
# print the JSON string representation of the object
print(FinancialBookCreateDto.to_json())

# convert the object into a dict
financial_book_create_dto_dict = financial_book_create_dto_instance.to_dict()
# create an instance of FinancialBookCreateDto from a dict
financial_book_create_dto_from_dict = FinancialBookCreateDto.from_dict(financial_book_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


