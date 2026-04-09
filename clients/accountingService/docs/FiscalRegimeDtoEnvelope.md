# FiscalRegimeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**FiscalRegimeDto**](FiscalRegimeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_regime_dto_envelope import FiscalRegimeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalRegimeDtoEnvelope from a JSON string
fiscal_regime_dto_envelope_instance = FiscalRegimeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(FiscalRegimeDtoEnvelope.to_json())

# convert the object into a dict
fiscal_regime_dto_envelope_dict = fiscal_regime_dto_envelope_instance.to_dict()
# create an instance of FiscalRegimeDtoEnvelope from a dict
fiscal_regime_dto_envelope_from_dict = FiscalRegimeDtoEnvelope.from_dict(fiscal_regime_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


