# CurrencyDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CurrencyDto]**](CurrencyDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.currency_dto_list_envelope import CurrencyDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyDtoListEnvelope from a JSON string
currency_dto_list_envelope_instance = CurrencyDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CurrencyDtoListEnvelope.to_json())

# convert the object into a dict
currency_dto_list_envelope_dict = currency_dto_list_envelope_instance.to_dict()
# create an instance of CurrencyDtoListEnvelope from a dict
currency_dto_list_envelope_from_dict = CurrencyDtoListEnvelope.from_dict(currency_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


