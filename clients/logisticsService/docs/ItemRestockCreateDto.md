# ItemRestockCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_restock_create_dto import ItemRestockCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRestockCreateDto from a JSON string
item_restock_create_dto_instance = ItemRestockCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemRestockCreateDto.to_json())

# convert the object into a dict
item_restock_create_dto_dict = item_restock_create_dto_instance.to_dict()
# create an instance of ItemRestockCreateDto from a dict
item_restock_create_dto_from_dict = ItemRestockCreateDto.from_dict(item_restock_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


