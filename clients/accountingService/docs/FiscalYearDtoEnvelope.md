# FiscalYearDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**FiscalYearDto**](FiscalYearDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.fiscal_year_dto_envelope import FiscalYearDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FiscalYearDtoEnvelope from a JSON string
fiscal_year_dto_envelope_instance = FiscalYearDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(FiscalYearDtoEnvelope.to_json())

# convert the object into a dict
fiscal_year_dto_envelope_dict = fiscal_year_dto_envelope_instance.to_dict()
# create an instance of FiscalYearDtoEnvelope from a dict
fiscal_year_dto_envelope_from_dict = FiscalYearDtoEnvelope.from_dict(fiscal_year_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


