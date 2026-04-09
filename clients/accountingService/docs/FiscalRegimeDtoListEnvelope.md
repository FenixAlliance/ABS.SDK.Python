# FiscalRegimeDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[FiscalRegimeDto]**](FiscalRegimeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_regime_dto_list_envelope import FiscalRegimeDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalRegimeDtoListEnvelope from a JSON string
fiscal_regime_dto_list_envelope_instance = FiscalRegimeDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(FiscalRegimeDtoListEnvelope.to_json())

# convert the object into a dict
fiscal_regime_dto_list_envelope_dict = fiscal_regime_dto_list_envelope_instance.to_dict()
# create an instance of FiscalRegimeDtoListEnvelope from a dict
fiscal_regime_dto_list_envelope_from_dict = FiscalRegimeDtoListEnvelope.from_dict(fiscal_regime_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


