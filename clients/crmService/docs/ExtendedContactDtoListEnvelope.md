# ExtendedContactDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ExtendedContactDto]**](ExtendedContactDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_contact_dto_list_envelope import ExtendedContactDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedContactDtoListEnvelope from a JSON string
extended_contact_dto_list_envelope_instance = ExtendedContactDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExtendedContactDtoListEnvelope.to_json())

# convert the object into a dict
extended_contact_dto_list_envelope_dict = extended_contact_dto_list_envelope_instance.to_dict()
# create an instance of ExtendedContactDtoListEnvelope from a dict
extended_contact_dto_list_envelope_from_dict = ExtendedContactDtoListEnvelope.from_dict(extended_contact_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


