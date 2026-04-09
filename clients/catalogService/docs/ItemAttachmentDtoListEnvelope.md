# ItemAttachmentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ItemAttachmentDto]**](ItemAttachmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_attachment_dto_list_envelope import ItemAttachmentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachmentDtoListEnvelope from a JSON string
item_attachment_dto_list_envelope_instance = ItemAttachmentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemAttachmentDtoListEnvelope.to_json())

# convert the object into a dict
item_attachment_dto_list_envelope_dict = item_attachment_dto_list_envelope_instance.to_dict()
# create an instance of ItemAttachmentDtoListEnvelope from a dict
item_attachment_dto_list_envelope_from_dict = ItemAttachmentDtoListEnvelope.from_dict(item_attachment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


