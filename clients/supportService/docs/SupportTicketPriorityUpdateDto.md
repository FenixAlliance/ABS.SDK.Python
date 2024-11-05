# SupportTicketPriorityUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_priority_update_dto import SupportTicketPriorityUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketPriorityUpdateDto from a JSON string
support_ticket_priority_update_dto_instance = SupportTicketPriorityUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketPriorityUpdateDto.to_json())

# convert the object into a dict
support_ticket_priority_update_dto_dict = support_ticket_priority_update_dto_instance.to_dict()
# create an instance of SupportTicketPriorityUpdateDto from a dict
support_ticket_priority_update_dto_from_dict = SupportTicketPriorityUpdateDto.from_dict(support_ticket_priority_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


