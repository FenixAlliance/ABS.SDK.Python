# ItemTagDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_tag_dto import ItemTagDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTagDto from a JSON string
item_tag_dto_instance = ItemTagDto.from_json(json)
# print the JSON string representation of the object
print(ItemTagDto.to_json())

# convert the object into a dict
item_tag_dto_dict = item_tag_dto_instance.to_dict()
# create an instance of ItemTagDto from a dict
item_tag_dto_from_dict = ItemTagDto.from_dict(item_tag_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


