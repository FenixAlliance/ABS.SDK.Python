# FinancialBookDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.financial_book_dto import FinancialBookDto

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialBookDto from a JSON string
financial_book_dto_instance = FinancialBookDto.from_json(json)
# print the JSON string representation of the object
print(FinancialBookDto.to_json())

# convert the object into a dict
financial_book_dto_dict = financial_book_dto_instance.to_dict()
# create an instance of FinancialBookDto from a dict
financial_book_dto_from_dict = FinancialBookDto.from_dict(financial_book_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


