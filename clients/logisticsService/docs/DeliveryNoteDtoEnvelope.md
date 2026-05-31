# DeliveryNoteDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**DeliveryNoteDto**](DeliveryNoteDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.delivery_note_dto_envelope import DeliveryNoteDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryNoteDtoEnvelope from a JSON string
delivery_note_dto_envelope_instance = DeliveryNoteDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(DeliveryNoteDtoEnvelope.to_json())

# convert the object into a dict
delivery_note_dto_envelope_dict = delivery_note_dto_envelope_instance.to_dict()
# create an instance of DeliveryNoteDtoEnvelope from a dict
delivery_note_dto_envelope_from_dict = DeliveryNoteDtoEnvelope.from_dict(delivery_note_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


