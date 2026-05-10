# ItemRestockDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**entry_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.item_restock_dto import ItemRestockDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRestockDto from a JSON string
item_restock_dto_instance = ItemRestockDto.from_json(json)
# print the JSON string representation of the object
print(ItemRestockDto.to_json())

# convert the object into a dict
item_restock_dto_dict = item_restock_dto_instance.to_dict()
# create an instance of ItemRestockDto from a dict
item_restock_dto_from_dict = ItemRestockDto.from_dict(item_restock_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


