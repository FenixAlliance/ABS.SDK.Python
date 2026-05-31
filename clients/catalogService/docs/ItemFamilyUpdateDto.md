# ItemFamilyUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_family_update_dto import ItemFamilyUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemFamilyUpdateDto from a JSON string
item_family_update_dto_instance = ItemFamilyUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemFamilyUpdateDto.to_json())

# convert the object into a dict
item_family_update_dto_dict = item_family_update_dto_instance.to_dict()
# create an instance of ItemFamilyUpdateDto from a dict
item_family_update_dto_from_dict = ItemFamilyUpdateDto.from_dict(item_family_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


