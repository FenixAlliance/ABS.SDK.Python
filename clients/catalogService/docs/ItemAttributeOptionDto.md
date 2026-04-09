# ItemAttributeOptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_attribute_option_dto import ItemAttributeOptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttributeOptionDto from a JSON string
item_attribute_option_dto_instance = ItemAttributeOptionDto.from_json(json)
# print the JSON string representation of the object
print(ItemAttributeOptionDto.to_json())

# convert the object into a dict
item_attribute_option_dto_dict = item_attribute_option_dto_instance.to_dict()
# create an instance of ItemAttributeOptionDto from a dict
item_attribute_option_dto_from_dict = ItemAttributeOptionDto.from_dict(item_attribute_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


