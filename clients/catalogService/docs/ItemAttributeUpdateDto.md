# ItemAttributeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_attribute_update_dto import ItemAttributeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttributeUpdateDto from a JSON string
item_attribute_update_dto_instance = ItemAttributeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemAttributeUpdateDto.to_json())

# convert the object into a dict
item_attribute_update_dto_dict = item_attribute_update_dto_instance.to_dict()
# create an instance of ItemAttributeUpdateDto from a dict
item_attribute_update_dto_from_dict = ItemAttributeUpdateDto.from_dict(item_attribute_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


