# CountryLanguageDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CountryLanguageDto]**](CountryLanguageDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.country_language_dto_list_envelope import CountryLanguageDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CountryLanguageDtoListEnvelope from a JSON string
country_language_dto_list_envelope_instance = CountryLanguageDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CountryLanguageDtoListEnvelope.to_json())

# convert the object into a dict
country_language_dto_list_envelope_dict = country_language_dto_list_envelope_instance.to_dict()
# create an instance of CountryLanguageDtoListEnvelope from a dict
country_language_dto_list_envelope_from_dict = CountryLanguageDtoListEnvelope.from_dict(country_language_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


