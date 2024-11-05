# CountryStateDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**CountryStateDto**](CountryStateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.country_state_dto_envelope import CountryStateDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CountryStateDtoEnvelope from a JSON string
country_state_dto_envelope_instance = CountryStateDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(CountryStateDtoEnvelope.to_json())

# convert the object into a dict
country_state_dto_envelope_dict = country_state_dto_envelope_instance.to_dict()
# create an instance of CountryStateDtoEnvelope from a dict
country_state_dto_envelope_from_dict = CountryStateDtoEnvelope.from_dict(country_state_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


