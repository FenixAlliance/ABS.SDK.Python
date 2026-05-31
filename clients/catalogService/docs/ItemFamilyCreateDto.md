# ItemFamilyCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_family_create_dto import ItemFamilyCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFamilyCreateDto from a JSON string
item_family_create_dto_instance = ItemFamilyCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemFamilyCreateDto.to_json())

# convert the object into a dict
item_family_create_dto_dict = item_family_create_dto_instance.to_dict()
# create an instance of ItemFamilyCreateDto from a dict
item_family_create_dto_from_dict = ItemFamilyCreateDto.from_dict(item_family_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


