# ForexRatesDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ForexRatesDto**](ForexRatesDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.forex_rates_dto_envelope import ForexRatesDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ForexRatesDtoEnvelope from a JSON string
forex_rates_dto_envelope_instance = ForexRatesDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ForexRatesDtoEnvelope.to_json())

# convert the object into a dict
forex_rates_dto_envelope_dict = forex_rates_dto_envelope_instance.to_dict()
# create an instance of ForexRatesDtoEnvelope from a dict
forex_rates_dto_envelope_from_dict = ForexRatesDtoEnvelope.from_dict(forex_rates_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


