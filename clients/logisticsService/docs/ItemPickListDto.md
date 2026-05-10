# ItemPickListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_pick_list_dto import ItemPickListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPickListDto from a JSON string
item_pick_list_dto_instance = ItemPickListDto.from_json(json)
# print the JSON string representation of the object
print(ItemPickListDto.to_json())

# convert the object into a dict
item_pick_list_dto_dict = item_pick_list_dto_instance.to_dict()
# create an instance of ItemPickListDto from a dict
item_pick_list_dto_from_dict = ItemPickListDto.from_dict(item_pick_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


