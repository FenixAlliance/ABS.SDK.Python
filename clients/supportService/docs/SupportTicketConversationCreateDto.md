# SupportTicketConversationCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**topic** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**closed_timestamp** | **datetime** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_conversation_create_dto import SupportTicketConversationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketConversationCreateDto from a JSON string
support_ticket_conversation_create_dto_instance = SupportTicketConversationCreateDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketConversationCreateDto.to_json())

# convert the object into a dict
support_ticket_conversation_create_dto_dict = support_ticket_conversation_create_dto_instance.to_dict()
# create an instance of SupportTicketConversationCreateDto from a dict
support_ticket_conversation_create_dto_from_dict = SupportTicketConversationCreateDto.from_dict(support_ticket_conversation_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


