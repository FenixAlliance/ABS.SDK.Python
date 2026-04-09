# ItemCategoryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**enable_for_courses** | **bool** |  | [optional] 
**enable_for_products** | **bool** |  | [optional] 
**enable_for_licenses** | **bool** |  | [optional] 
**enable_for_services** | **bool** |  | [optional] 
**enable_for_subscriptions** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.item_category_update_dto import ItemCategoryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCategoryUpdateDto from a JSON string
item_category_update_dto_instance = ItemCategoryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemCategoryUpdateDto.to_json())

# convert the object into a dict
item_category_update_dto_dict = item_category_update_dto_instance.to_dict()
# create an instance of ItemCategoryUpdateDto from a dict
item_category_update_dto_from_dict = ItemCategoryUpdateDto.from_dict(item_category_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


