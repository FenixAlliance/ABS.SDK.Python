# CurrencyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**country** | [**CountryDto**](CountryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.currency_dto import CurrencyDto

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyDto from a JSON string
currency_dto_instance = CurrencyDto.from_json(json)
# print the JSON string representation of the object
print(CurrencyDto.to_json())

# convert the object into a dict
currency_dto_dict = currency_dto_instance.to_dict()
# create an instance of CurrencyDto from a dict
currency_dto_from_dict = CurrencyDto.from_dict(currency_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


