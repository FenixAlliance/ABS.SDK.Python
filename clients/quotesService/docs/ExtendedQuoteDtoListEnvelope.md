# ExtendedQuoteDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ExtendedQuoteDto]**](ExtendedQuoteDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_quote_dto_list_envelope import ExtendedQuoteDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedQuoteDtoListEnvelope from a JSON string
extended_quote_dto_list_envelope_instance = ExtendedQuoteDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExtendedQuoteDtoListEnvelope.to_json())

# convert the object into a dict
extended_quote_dto_list_envelope_dict = extended_quote_dto_list_envelope_instance.to_dict()
# create an instance of ExtendedQuoteDtoListEnvelope from a dict
extended_quote_dto_list_envelope_from_dict = ExtendedQuoteDtoListEnvelope.from_dict(extended_quote_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


