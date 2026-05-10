# ItemRestockDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ItemRestockDto**](ItemRestockDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_restock_dto_envelope import ItemRestockDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRestockDtoEnvelope from a JSON string
item_restock_dto_envelope_instance = ItemRestockDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemRestockDtoEnvelope.to_json())

# convert the object into a dict
item_restock_dto_envelope_dict = item_restock_dto_envelope_instance.to_dict()
# create an instance of ItemRestockDtoEnvelope from a dict
item_restock_dto_envelope_from_dict = ItemRestockDtoEnvelope.from_dict(item_restock_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


