# EmailGroupDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**EmailGroupDto**](EmailGroupDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_group_dto_envelope import EmailGroupDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmailGroupDtoEnvelope from a JSON string
email_group_dto_envelope_instance = EmailGroupDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmailGroupDtoEnvelope.to_json())

# convert the object into a dict
email_group_dto_envelope_dict = email_group_dto_envelope_instance.to_dict()
# create an instance of EmailGroupDtoEnvelope from a dict
email_group_dto_envelope_from_dict = EmailGroupDtoEnvelope.from_dict(email_group_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


