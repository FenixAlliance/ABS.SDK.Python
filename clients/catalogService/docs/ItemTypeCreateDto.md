# ItemTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**plural_title** | **str** |  | [optional] 
**singular_title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**google_category_taxonomy** | **str** |  | [optional] 
**item_category_id** | **str** |  | 
**item_google_category_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_type_create_dto import ItemTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTypeCreateDto from a JSON string
item_type_create_dto_instance = ItemTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemTypeCreateDto.to_json())

# convert the object into a dict
item_type_create_dto_dict = item_type_create_dto_instance.to_dict()
# create an instance of ItemTypeCreateDto from a dict
item_type_create_dto_from_dict = ItemTypeCreateDto.from_dict(item_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


