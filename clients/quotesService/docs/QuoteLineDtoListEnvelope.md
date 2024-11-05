# QuoteLineDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[QuoteLineDto]**](QuoteLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.quote_line_dto_list_envelope import QuoteLineDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLineDtoListEnvelope from a JSON string
quote_line_dto_list_envelope_instance = QuoteLineDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(QuoteLineDtoListEnvelope.to_json())

# convert the object into a dict
quote_line_dto_list_envelope_dict = quote_line_dto_list_envelope_instance.to_dict()
# create an instance of QuoteLineDtoListEnvelope from a dict
quote_line_dto_list_envelope_from_dict = QuoteLineDtoListEnvelope.from_dict(quote_line_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


