# WishListItemRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**wish_list_id** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.wish_list_item_record_dto import WishListItemRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of WishListItemRecordDto from a JSON string
wish_list_item_record_dto_instance = WishListItemRecordDto.from_json(json)
# print the JSON string representation of the object
print(WishListItemRecordDto.to_json())

# convert the object into a dict
wish_list_item_record_dto_dict = wish_list_item_record_dto_instance.to_dict()
# create an instance of WishListItemRecordDto from a dict
wish_list_item_record_dto_from_dict = WishListItemRecordDto.from_dict(wish_list_item_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


