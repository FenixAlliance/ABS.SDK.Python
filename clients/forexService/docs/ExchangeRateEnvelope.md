# ExchangeRateEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ExchangeRate**](ExchangeRate.md) |  | [optional] 

## Example

```python
from openapi_client.models.exchange_rate_envelope import ExchangeRateEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRateEnvelope from a JSON string
exchange_rate_envelope_instance = ExchangeRateEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExchangeRateEnvelope.to_json())

# convert the object into a dict
exchange_rate_envelope_dict = exchange_rate_envelope_instance.to_dict()
# create an instance of ExchangeRateEnvelope from a dict
exchange_rate_envelope_from_dict = ExchangeRateEnvelope.from_dict(exchange_rate_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


