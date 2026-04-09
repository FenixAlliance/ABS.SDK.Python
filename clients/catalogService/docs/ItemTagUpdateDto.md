# ItemTagUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_tag_update_dto import ItemTagUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTagUpdateDto from a JSON string
item_tag_update_dto_instance = ItemTagUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemTagUpdateDto.to_json())

# convert the object into a dict
item_tag_update_dto_dict = item_tag_update_dto_instance.to_dict()
# create an instance of ItemTagUpdateDto from a dict
item_tag_update_dto_from_dict = ItemTagUpdateDto.from_dict(item_tag_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


