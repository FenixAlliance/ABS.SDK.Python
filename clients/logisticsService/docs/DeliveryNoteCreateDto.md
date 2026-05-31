# DeliveryNoteCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**proof_of_delivery_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.delivery_note_create_dto import DeliveryNoteCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryNoteCreateDto from a JSON string
delivery_note_create_dto_instance = DeliveryNoteCreateDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryNoteCreateDto.to_json())

# convert the object into a dict
delivery_note_create_dto_dict = delivery_note_create_dto_instance.to_dict()
# create an instance of DeliveryNoteCreateDto from a dict
delivery_note_create_dto_from_dict = DeliveryNoteCreateDto.from_dict(delivery_note_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


