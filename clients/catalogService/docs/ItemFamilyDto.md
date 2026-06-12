# ItemFamilyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_family_dto import ItemFamilyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFamilyDto from a JSON string
item_family_dto_instance = ItemFamilyDto.from_json(json)
# print the JSON string representation of the object
print(ItemFamilyDto.to_json())

# convert the object into a dict
item_family_dto_dict = item_family_dto_instance.to_dict()
# create an instance of ItemFamilyDto from a dict
item_family_dto_from_dict = ItemFamilyDto.from_dict(item_family_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


