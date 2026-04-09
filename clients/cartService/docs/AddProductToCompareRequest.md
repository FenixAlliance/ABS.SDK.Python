# AddProductToCompareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**cart_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.add_product_to_compare_request import AddProductToCompareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddProductToCompareRequest from a JSON string
add_product_to_compare_request_instance = AddProductToCompareRequest.from_json(json)
# print the JSON string representation of the object
print(AddProductToCompareRequest.to_json())

# convert the object into a dict
add_product_to_compare_request_dict = add_product_to_compare_request_instance.to_dict()
# create an instance of AddProductToCompareRequest from a dict
add_product_to_compare_request_from_dict = AddProductToCompareRequest.from_dict(add_product_to_compare_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


