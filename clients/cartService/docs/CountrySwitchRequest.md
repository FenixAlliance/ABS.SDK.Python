# CountrySwitchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.country_switch_request import CountrySwitchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CountrySwitchRequest from a JSON string
country_switch_request_instance = CountrySwitchRequest.from_json(json)
# print the JSON string representation of the object
print(CountrySwitchRequest.to_json())

# convert the object into a dict
country_switch_request_dict = country_switch_request_instance.to_dict()
# create an instance of CountrySwitchRequest from a dict
country_switch_request_from_dict = CountrySwitchRequest.from_dict(country_switch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


