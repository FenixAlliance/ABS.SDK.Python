# WishListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.wish_list_dto import WishListDto

# TODO update the JSON string below
json = "{}"
# create an instance of WishListDto from a JSON string
wish_list_dto_instance = WishListDto.from_json(json)
# print the JSON string representation of the object
print(WishListDto.to_json())

# convert the object into a dict
wish_list_dto_dict = wish_list_dto_instance.to_dict()
# create an instance of WishListDto from a dict
wish_list_dto_from_dict = WishListDto.from_dict(wish_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


