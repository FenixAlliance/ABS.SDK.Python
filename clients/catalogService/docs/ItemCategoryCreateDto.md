# ItemCategoryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**business_id** | **str** |  | 
**business_profile_record_id** | **str** |  | [optional] 
**parent_item_category_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_category_create_dto import ItemCategoryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCategoryCreateDto from a JSON string
item_category_create_dto_instance = ItemCategoryCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemCategoryCreateDto.to_json())

# convert the object into a dict
item_category_create_dto_dict = item_category_create_dto_instance.to_dict()
# create an instance of ItemCategoryCreateDto from a dict
item_category_create_dto_from_dict = ItemCategoryCreateDto.from_dict(item_category_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


