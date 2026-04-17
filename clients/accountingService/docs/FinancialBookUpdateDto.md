# FinancialBookUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.financial_book_update_dto import FinancialBookUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialBookUpdateDto from a JSON string
financial_book_update_dto_instance = FinancialBookUpdateDto.from_json(json)
# print the JSON string representation of the object
print(FinancialBookUpdateDto.to_json())

# convert the object into a dict
financial_book_update_dto_dict = financial_book_update_dto_instance.to_dict()
# create an instance of FinancialBookUpdateDto from a dict
financial_book_update_dto_from_dict = FinancialBookUpdateDto.from_dict(financial_book_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


