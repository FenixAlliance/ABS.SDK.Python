# NewWishListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.new_wish_list_request import NewWishListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NewWishListRequest from a JSON string
new_wish_list_request_instance = NewWishListRequest.from_json(json)
# print the JSON string representation of the object
print(NewWishListRequest.to_json())

# convert the object into a dict
new_wish_list_request_dict = new_wish_list_request_instance.to_dict()
# create an instance of NewWishListRequest from a dict
new_wish_list_request_from_dict = NewWishListRequest.from_dict(new_wish_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


