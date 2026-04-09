# ItemTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**plural_title** | **str** |  | 
**singular_title** | **str** |  | 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**google_category_taxonomy** | **str** |  | [optional] 
**business_id** | **str** |  | 
**item_category_id** | **str** |  | 
**item_google_category_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_type_dto import ItemTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTypeDto from a JSON string
item_type_dto_instance = ItemTypeDto.from_json(json)
# print the JSON string representation of the object
print(ItemTypeDto.to_json())

# convert the object into a dict
item_type_dto_dict = item_type_dto_instance.to_dict()
# create an instance of ItemTypeDto from a dict
item_type_dto_from_dict = ItemTypeDto.from_dict(item_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


