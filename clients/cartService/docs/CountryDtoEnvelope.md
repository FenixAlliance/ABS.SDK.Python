# CountryDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**CountryDto**](CountryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.country_dto_envelope import CountryDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CountryDtoEnvelope from a JSON string
country_dto_envelope_instance = CountryDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(CountryDtoEnvelope.to_json())

# convert the object into a dict
country_dto_envelope_dict = country_dto_envelope_instance.to_dict()
# create an instance of CountryDtoEnvelope from a dict
country_dto_envelope_from_dict = CountryDtoEnvelope.from_dict(country_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


