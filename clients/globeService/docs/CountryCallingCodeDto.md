# CountryCallingCodeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**calling_code** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.country_calling_code_dto import CountryCallingCodeDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountryCallingCodeDto from a JSON string
country_calling_code_dto_instance = CountryCallingCodeDto.from_json(json)
# print the JSON string representation of the object
print(CountryCallingCodeDto.to_json())

# convert the object into a dict
country_calling_code_dto_dict = country_calling_code_dto_instance.to_dict()
# create an instance of CountryCallingCodeDto from a dict
country_calling_code_dto_from_dict = CountryCallingCodeDto.from_dict(country_calling_code_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


