# ContactProfileDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ContactProfileDto]**](ContactProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.contact_profile_dto_list_envelope import ContactProfileDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ContactProfileDtoListEnvelope from a JSON string
contact_profile_dto_list_envelope_instance = ContactProfileDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ContactProfileDtoListEnvelope.to_json())

# convert the object into a dict
contact_profile_dto_list_envelope_dict = contact_profile_dto_list_envelope_instance.to_dict()
# create an instance of ContactProfileDtoListEnvelope from a dict
contact_profile_dto_list_envelope_from_dict = ContactProfileDtoListEnvelope.from_dict(contact_profile_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


