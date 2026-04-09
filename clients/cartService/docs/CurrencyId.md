# CurrencyId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] [readonly] 
**code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.currency_id import CurrencyId

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyId from a JSON string
currency_id_instance = CurrencyId.from_json(json)
# print the JSON string representation of the object
print(CurrencyId.to_json())

# convert the object into a dict
currency_id_dict = currency_id_instance.to_dict()
# create an instance of CurrencyId from a dict
currency_id_from_dict = CurrencyId.from_dict(currency_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


