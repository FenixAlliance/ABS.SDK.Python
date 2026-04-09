# WishListUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.wish_list_update_dto import WishListUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of WishListUpdateDto from a JSON string
wish_list_update_dto_instance = WishListUpdateDto.from_json(json)
# print the JSON string representation of the object
print(WishListUpdateDto.to_json())

# convert the object into a dict
wish_list_update_dto_dict = wish_list_update_dto_instance.to_dict()
# create an instance of WishListUpdateDto from a dict
wish_list_update_dto_from_dict = WishListUpdateDto.from_dict(wish_list_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


