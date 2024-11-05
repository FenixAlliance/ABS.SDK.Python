# ContactDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ContactDto**](ContactDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.contact_dto_envelope import ContactDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDtoEnvelope from a JSON string
contact_dto_envelope_instance = ContactDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ContactDtoEnvelope.to_json())

# convert the object into a dict
contact_dto_envelope_dict = contact_dto_envelope_instance.to_dict()
# create an instance of ContactDtoEnvelope from a dict
contact_dto_envelope_from_dict = ContactDtoEnvelope.from_dict(contact_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


