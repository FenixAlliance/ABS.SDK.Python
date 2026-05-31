# ItemAttributeOptionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**item_attribute_id** | **str** |  | 

## Example

```python
from openapi_client.models.item_attribute_option_create_dto import ItemAttributeOptionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttributeOptionCreateDto from a JSON string
item_attribute_option_create_dto_instance = ItemAttributeOptionCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemAttributeOptionCreateDto.to_json())

# convert the object into a dict
item_attribute_option_create_dto_dict = item_attribute_option_create_dto_instance.to_dict()
# create an instance of ItemAttributeOptionCreateDto from a dict
item_attribute_option_create_dto_from_dict = ItemAttributeOptionCreateDto.from_dict(item_attribute_option_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


