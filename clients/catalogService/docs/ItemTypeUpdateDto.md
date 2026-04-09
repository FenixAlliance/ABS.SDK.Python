# ItemTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plural_title** | **str** |  | [optional] 
**singular_title** | **str** |  | 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**google_category_taxonomy** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_type_update_dto import ItemTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTypeUpdateDto from a JSON string
item_type_update_dto_instance = ItemTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemTypeUpdateDto.to_json())

# convert the object into a dict
item_type_update_dto_dict = item_type_update_dto_instance.to_dict()
# create an instance of ItemTypeUpdateDto from a dict
item_type_update_dto_from_dict = ItemTypeUpdateDto.from_dict(item_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


