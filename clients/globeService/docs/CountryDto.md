# CountryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**iso3** | **str** |  | [optional] 
**iso2** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**native_name** | **str** |  | [optional] 
**flag_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.country_dto import CountryDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountryDto from a JSON string
country_dto_instance = CountryDto.from_json(json)
# print the JSON string representation of the object
print(CountryDto.to_json())

# convert the object into a dict
country_dto_dict = country_dto_instance.to_dict()
# create an instance of CountryDto from a dict
country_dto_from_dict = CountryDto.from_dict(country_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


