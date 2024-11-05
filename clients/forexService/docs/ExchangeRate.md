# ExchangeRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**Money**](Money.md) |  | [optional] 
**target** | [**Money**](Money.md) |  | [optional] 
**rate** | [**Money**](Money.md) |  | [optional] 

## Example

```python
from openapi_client.models.exchange_rate import ExchangeRate

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRate from a JSON string
exchange_rate_instance = ExchangeRate.from_json(json)
# print the JSON string representation of the object
print(ExchangeRate.to_json())

# convert the object into a dict
exchange_rate_dict = exchange_rate_instance.to_dict()
# create an instance of ExchangeRate from a dict
exchange_rate_from_dict = ExchangeRate.from_dict(exchange_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


