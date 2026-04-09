# FiscalPeriodDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**FiscalPeriodDto**](FiscalPeriodDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_period_dto_envelope import FiscalPeriodDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalPeriodDtoEnvelope from a JSON string
fiscal_period_dto_envelope_instance = FiscalPeriodDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(FiscalPeriodDtoEnvelope.to_json())

# convert the object into a dict
fiscal_period_dto_envelope_dict = fiscal_period_dto_envelope_instance.to_dict()
# create an instance of FiscalPeriodDtoEnvelope from a dict
fiscal_period_dto_envelope_from_dict = FiscalPeriodDtoEnvelope.from_dict(fiscal_period_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


