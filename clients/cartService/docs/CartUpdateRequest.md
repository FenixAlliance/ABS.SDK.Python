# CartUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cart_update_request import CartUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CartUpdateRequest from a JSON string
cart_update_request_instance = CartUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CartUpdateRequest.to_json())

# convert the object into a dict
cart_update_request_dict = cart_update_request_instance.to_dict()
# create an instance of CartUpdateRequest from a dict
cart_update_request_from_dict = CartUpdateRequest.from_dict(cart_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


