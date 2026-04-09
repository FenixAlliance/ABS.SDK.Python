# CurrencySwitchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.currency_switch_request import CurrencySwitchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencySwitchRequest from a JSON string
currency_switch_request_instance = CurrencySwitchRequest.from_json(json)
# print the JSON string representation of the object
print(CurrencySwitchRequest.to_json())

# convert the object into a dict
currency_switch_request_dict = currency_switch_request_instance.to_dict()
# create an instance of CurrencySwitchRequest from a dict
currency_switch_request_from_dict = CurrencySwitchRequest.from_dict(currency_switch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


