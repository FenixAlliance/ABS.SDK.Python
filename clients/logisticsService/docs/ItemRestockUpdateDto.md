# ItemRestockUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_restock_update_dto import ItemRestockUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRestockUpdateDto from a JSON string
item_restock_update_dto_instance = ItemRestockUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemRestockUpdateDto.to_json())

# convert the object into a dict
item_restock_update_dto_dict = item_restock_update_dto_instance.to_dict()
# create an instance of ItemRestockUpdateDto from a dict
item_restock_update_dto_from_dict = ItemRestockUpdateDto.from_dict(item_restock_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


