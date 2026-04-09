# ItemAttributeDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ItemAttributeDto]**](ItemAttributeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_attribute_dto_list_envelope import ItemAttributeDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttributeDtoListEnvelope from a JSON string
item_attribute_dto_list_envelope_instance = ItemAttributeDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemAttributeDtoListEnvelope.to_json())

# convert the object into a dict
item_attribute_dto_list_envelope_dict = item_attribute_dto_list_envelope_instance.to_dict()
# create an instance of ItemAttributeDtoListEnvelope from a dict
item_attribute_dto_list_envelope_from_dict = ItemAttributeDtoListEnvelope.from_dict(item_attribute_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


