# ContactDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ContactDto]**](ContactDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.contact_dto_list_envelope import ContactDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDtoListEnvelope from a JSON string
contact_dto_list_envelope_instance = ContactDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ContactDtoListEnvelope.to_json())

# convert the object into a dict
contact_dto_list_envelope_dict = contact_dto_list_envelope_instance.to_dict()
# create an instance of ContactDtoListEnvelope from a dict
contact_dto_list_envelope_from_dict = ContactDtoListEnvelope.from_dict(contact_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


