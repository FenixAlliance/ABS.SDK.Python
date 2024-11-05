# CurrencyDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**CurrencyDto**](CurrencyDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.currency_dto_envelope import CurrencyDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyDtoEnvelope from a JSON string
currency_dto_envelope_instance = CurrencyDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(CurrencyDtoEnvelope.to_json())

# convert the object into a dict
currency_dto_envelope_dict = currency_dto_envelope_instance.to_dict()
# create an instance of CurrencyDtoEnvelope from a dict
currency_dto_envelope_from_dict = CurrencyDtoEnvelope.from_dict(currency_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


