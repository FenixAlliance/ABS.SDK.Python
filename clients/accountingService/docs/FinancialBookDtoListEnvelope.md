# FinancialBookDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[FinancialBookDto]**](FinancialBookDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.financial_book_dto_list_envelope import FinancialBookDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialBookDtoListEnvelope from a JSON string
financial_book_dto_list_envelope_instance = FinancialBookDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(FinancialBookDtoListEnvelope.to_json())

# convert the object into a dict
financial_book_dto_list_envelope_dict = financial_book_dto_list_envelope_instance.to_dict()
# create an instance of FinancialBookDtoListEnvelope from a dict
financial_book_dto_list_envelope_from_dict = FinancialBookDtoListEnvelope.from_dict(financial_book_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


