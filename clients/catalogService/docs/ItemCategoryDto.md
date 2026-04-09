# ItemCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**enable_for_courses** | **bool** |  | [optional] 
**enable_for_products** | **bool** |  | [optional] 
**enable_for_licenses** | **bool** |  | [optional] 
**enable_for_services** | **bool** |  | [optional] 
**enable_for_subscriptions** | **bool** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**parent_item_category_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_category_dto import ItemCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCategoryDto from a JSON string
item_category_dto_instance = ItemCategoryDto.from_json(json)
# print the JSON string representation of the object
print(ItemCategoryDto.to_json())

# convert the object into a dict
item_category_dto_dict = item_category_dto_instance.to_dict()
# create an instance of ItemCategoryDto from a dict
item_category_dto_from_dict = ItemCategoryDto.from_dict(item_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


