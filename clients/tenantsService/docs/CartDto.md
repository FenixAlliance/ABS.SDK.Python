# CartDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**total** | **float** |  | [optional] 
**taxes** | **float** |  | [optional] 
**freight** | **float** |  | [optional] 
**sub_total** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**item_cart_records_count** | **int** |  | [optional] 
**item_to_compare_records_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.cart_dto import CartDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartDto from a JSON string
cart_dto_instance = CartDto.from_json(json)
# print the JSON string representation of the object
print(CartDto.to_json())

# convert the object into a dict
cart_dto_dict = cart_dto_instance.to_dict()
# create an instance of CartDto from a dict
cart_dto_from_dict = CartDto.from_dict(cart_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


