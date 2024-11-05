# SupportTicketConversationDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SupportTicketConversationDto**](SupportTicketConversationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_conversation_dto_envelope import SupportTicketConversationDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketConversationDtoEnvelope from a JSON string
support_ticket_conversation_dto_envelope_instance = SupportTicketConversationDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupportTicketConversationDtoEnvelope.to_json())

# convert the object into a dict
support_ticket_conversation_dto_envelope_dict = support_ticket_conversation_dto_envelope_instance.to_dict()
# create an instance of SupportTicketConversationDtoEnvelope from a dict
support_ticket_conversation_dto_envelope_from_dict = SupportTicketConversationDtoEnvelope.from_dict(support_ticket_conversation_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


