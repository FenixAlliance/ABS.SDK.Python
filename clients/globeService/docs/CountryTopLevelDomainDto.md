# CountryTopLevelDomainDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.country_top_level_domain_dto import CountryTopLevelDomainDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountryTopLevelDomainDto from a JSON string
country_top_level_domain_dto_instance = CountryTopLevelDomainDto.from_json(json)
# print the JSON string representation of the object
print(CountryTopLevelDomainDto.to_json())

# convert the object into a dict
country_top_level_domain_dto_dict = country_top_level_domain_dto_instance.to_dict()
# create an instance of CountryTopLevelDomainDto from a dict
country_top_level_domain_dto_from_dict = CountryTopLevelDomainDto.from_dict(country_top_level_domain_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


