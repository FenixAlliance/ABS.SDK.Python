# QuoteLineDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**QuoteLineDto**](QuoteLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.quote_line_dto_envelope import QuoteLineDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLineDtoEnvelope from a JSON string
quote_line_dto_envelope_instance = QuoteLineDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(QuoteLineDtoEnvelope.to_json())

# convert the object into a dict
quote_line_dto_envelope_dict = quote_line_dto_envelope_instance.to_dict()
# create an instance of QuoteLineDtoEnvelope from a dict
quote_line_dto_envelope_from_dict = QuoteLineDtoEnvelope.from_dict(quote_line_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


