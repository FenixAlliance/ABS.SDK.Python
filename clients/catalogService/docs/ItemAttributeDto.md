# ItemAttributeDto


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
from openapi_client.models.item_attribute_dto import ItemAttributeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttributeDto from a JSON string
item_attribute_dto_instance = ItemAttributeDto.from_json(json)
# print the JSON string representation of the object
print(ItemAttributeDto.to_json())

# convert the object into a dict
item_attribute_dto_dict = item_attribute_dto_instance.to_dict()
# create an instance of ItemAttributeDto from a dict
item_attribute_dto_from_dict = ItemAttributeDto.from_dict(item_attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


