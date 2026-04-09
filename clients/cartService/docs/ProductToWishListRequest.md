# ProductToWishListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wish_list_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.product_to_wish_list_request import ProductToWishListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductToWishListRequest from a JSON string
product_to_wish_list_request_instance = ProductToWishListRequest.from_json(json)
# print the JSON string representation of the object
print(ProductToWishListRequest.to_json())

# convert the object into a dict
product_to_wish_list_request_dict = product_to_wish_list_request_instance.to_dict()
# create an instance of ProductToWishListRequest from a dict
product_to_wish_list_request_from_dict = ProductToWishListRequest.from_dict(product_to_wish_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


