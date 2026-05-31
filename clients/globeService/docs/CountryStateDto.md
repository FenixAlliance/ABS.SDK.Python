# CountryStateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.country_state_dto import CountryStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountryStateDto from a JSON string
country_state_dto_instance = CountryStateDto.from_json(json)
# print the JSON string representation of the object
print(CountryStateDto.to_json())

# convert the object into a dict
country_state_dto_dict = country_state_dto_instance.to_dict()
# create an instance of CountryStateDto from a dict
country_state_dto_from_dict = CountryStateDto.from_dict(country_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


