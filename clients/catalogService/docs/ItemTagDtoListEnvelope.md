# ItemTagDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ItemTagDto]**](ItemTagDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_tag_dto_list_envelope import ItemTagDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTagDtoListEnvelope from a JSON string
item_tag_dto_list_envelope_instance = ItemTagDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemTagDtoListEnvelope.to_json())

# convert the object into a dict
item_tag_dto_list_envelope_dict = item_tag_dto_list_envelope_instance.to_dict()
# create an instance of ItemTagDtoListEnvelope from a dict
item_tag_dto_list_envelope_from_dict = ItemTagDtoListEnvelope.from_dict(item_tag_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


