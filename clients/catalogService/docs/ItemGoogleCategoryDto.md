# ItemGoogleCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**path** | **str** |  | 
**icon** | **str** |  | [optional] 
**name** | **str** |  | 
**disabled** | **bool** |  | [optional] 
**featured** | **bool** |  | [optional] 
**display_on_menu** | **bool** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**menu_image** | **str** |  | [optional] 
**banner_code** | **str** |  | [optional] 
**banner_image** | **str** |  | [optional] 
**primary_image** | **str** |  | [optional] 
**parent_category_id** | **str** |  | [optional] 
**starting_at_amount_in_usd** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.item_google_category_dto import ItemGoogleCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemGoogleCategoryDto from a JSON string
item_google_category_dto_instance = ItemGoogleCategoryDto.from_json(json)
# print the JSON string representation of the object
print(ItemGoogleCategoryDto.to_json())

# convert the object into a dict
item_google_category_dto_dict = item_google_category_dto_instance.to_dict()
# create an instance of ItemGoogleCategoryDto from a dict
item_google_category_dto_from_dict = ItemGoogleCategoryDto.from_dict(item_google_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


