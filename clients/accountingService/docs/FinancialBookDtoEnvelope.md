# FinancialBookDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**FinancialBookDto**](FinancialBookDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.financial_book_dto_envelope import FinancialBookDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialBookDtoEnvelope from a JSON string
financial_book_dto_envelope_instance = FinancialBookDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(FinancialBookDtoEnvelope.to_json())

# convert the object into a dict
financial_book_dto_envelope_dict = financial_book_dto_envelope_instance.to_dict()
# create an instance of FinancialBookDtoEnvelope from a dict
financial_book_dto_envelope_from_dict = FinancialBookDtoEnvelope.from_dict(financial_book_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


