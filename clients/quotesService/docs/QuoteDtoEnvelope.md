# QuoteDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**QuoteDto**](QuoteDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.quote_dto_envelope import QuoteDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDtoEnvelope from a JSON string
quote_dto_envelope_instance = QuoteDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(QuoteDtoEnvelope.to_json())

# convert the object into a dict
quote_dto_envelope_dict = quote_dto_envelope_instance.to_dict()
# create an instance of QuoteDtoEnvelope from a dict
quote_dto_envelope_from_dict = QuoteDtoEnvelope.from_dict(quote_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


