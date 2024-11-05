# SupportTicketConversationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**support_ticket_id** | **str** |  | [optional] 
**topic** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**closed_timestamp** | **datetime** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_conversation_dto import SupportTicketConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketConversationDto from a JSON string
support_ticket_conversation_dto_instance = SupportTicketConversationDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketConversationDto.to_json())

# convert the object into a dict
support_ticket_conversation_dto_dict = support_ticket_conversation_dto_instance.to_dict()
# create an instance of SupportTicketConversationDto from a dict
support_ticket_conversation_dto_from_dict = SupportTicketConversationDto.from_dict(support_ticket_conversation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


