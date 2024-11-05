# CountryStateDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CountryStateDto]**](CountryStateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.country_state_dto_list_envelope import CountryStateDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CountryStateDtoListEnvelope from a JSON string
country_state_dto_list_envelope_instance = CountryStateDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CountryStateDtoListEnvelope.to_json())

# convert the object into a dict
country_state_dto_list_envelope_dict = country_state_dto_list_envelope_instance.to_dict()
# create an instance of CountryStateDtoListEnvelope from a dict
country_state_dto_list_envelope_from_dict = CountryStateDtoListEnvelope.from_dict(country_state_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


