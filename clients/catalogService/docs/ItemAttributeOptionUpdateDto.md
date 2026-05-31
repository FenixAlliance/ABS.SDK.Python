# ItemAttributeOptionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_attribute_option_update_dto import ItemAttributeOptionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttributeOptionUpdateDto from a JSON string
item_attribute_option_update_dto_instance = ItemAttributeOptionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemAttributeOptionUpdateDto.to_json())

# convert the object into a dict
item_attribute_option_update_dto_dict = item_attribute_option_update_dto_instance.to_dict()
# create an instance of ItemAttributeOptionUpdateDto from a dict
item_attribute_option_update_dto_from_dict = ItemAttributeOptionUpdateDto.from_dict(item_attribute_option_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


