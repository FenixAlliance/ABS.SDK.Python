# CountryLanguageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**iso639_1** | **str** |  | [optional] 
**iso639_2** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**language_native_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.country_language_dto import CountryLanguageDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountryLanguageDto from a JSON string
country_language_dto_instance = CountryLanguageDto.from_json(json)
# print the JSON string representation of the object
print(CountryLanguageDto.to_json())

# convert the object into a dict
country_language_dto_dict = country_language_dto_instance.to_dict()
# create an instance of CountryLanguageDto from a dict
country_language_dto_from_dict = CountryLanguageDto.from_dict(country_language_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


