# CartOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_guest_cart** | **bool** |  | [optional] 
**product_placeholder_image** | **str** |  | [optional] 
**redirect_to_cart_page_after_adding_products** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.cart_options import CartOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CartOptions from a JSON string
cart_options_instance = CartOptions.from_json(json)
# print the JSON string representation of the object
print(CartOptions.to_json())

# convert the object into a dict
cart_options_dict = cart_options_instance.to_dict()
# create an instance of CartOptions from a dict
cart_options_from_dict = CartOptions.from_dict(cart_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


