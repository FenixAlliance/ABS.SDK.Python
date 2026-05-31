# DeliveryNoteUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**proof_of_delivery_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.delivery_note_update_dto import DeliveryNoteUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryNoteUpdateDto from a JSON string
delivery_note_update_dto_instance = DeliveryNoteUpdateDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryNoteUpdateDto.to_json())

# convert the object into a dict
delivery_note_update_dto_dict = delivery_note_update_dto_instance.to_dict()
# create an instance of DeliveryNoteUpdateDto from a dict
delivery_note_update_dto_from_dict = DeliveryNoteUpdateDto.from_dict(delivery_note_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


