# LedgerDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**LedgerDto**](LedgerDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.ledger_dto_envelope import LedgerDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerDtoEnvelope from a JSON string
ledger_dto_envelope_instance = LedgerDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(LedgerDtoEnvelope.to_json())

# convert the object into a dict
ledger_dto_envelope_dict = ledger_dto_envelope_instance.to_dict()
# create an instance of LedgerDtoEnvelope from a dict
ledger_dto_envelope_from_dict = LedgerDtoEnvelope.from_dict(ledger_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


