# DeliveryNoteDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[DeliveryNoteDto]**](DeliveryNoteDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.delivery_note_dto_list_envelope import DeliveryNoteDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryNoteDtoListEnvelope from a JSON string
delivery_note_dto_list_envelope_instance = DeliveryNoteDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(DeliveryNoteDtoListEnvelope.to_json())

# convert the object into a dict
delivery_note_dto_list_envelope_dict = delivery_note_dto_list_envelope_instance.to_dict()
# create an instance of DeliveryNoteDtoListEnvelope from a dict
delivery_note_dto_list_envelope_from_dict = DeliveryNoteDtoListEnvelope.from_dict(delivery_note_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


