# ItemTagCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_tag_create_dto import ItemTagCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTagCreateDto from a JSON string
item_tag_create_dto_instance = ItemTagCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemTagCreateDto.to_json())

# convert the object into a dict
item_tag_create_dto_dict = item_tag_create_dto_instance.to_dict()
# create an instance of ItemTagCreateDto from a dict
item_tag_create_dto_from_dict = ItemTagCreateDto.from_dict(item_tag_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


