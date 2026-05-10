# ItemRestockDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ItemRestockDto]**](ItemRestockDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_restock_dto_list_envelope import ItemRestockDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRestockDtoListEnvelope from a JSON string
item_restock_dto_list_envelope_instance = ItemRestockDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemRestockDtoListEnvelope.to_json())

# convert the object into a dict
item_restock_dto_list_envelope_dict = item_restock_dto_list_envelope_instance.to_dict()
# create an instance of ItemRestockDtoListEnvelope from a dict
item_restock_dto_list_envelope_from_dict = ItemRestockDtoListEnvelope.from_dict(item_restock_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


