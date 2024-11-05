# SupportTicketPriorityCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_priority_create_dto import SupportTicketPriorityCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketPriorityCreateDto from a JSON string
support_ticket_priority_create_dto_instance = SupportTicketPriorityCreateDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketPriorityCreateDto.to_json())

# convert the object into a dict
support_ticket_priority_create_dto_dict = support_ticket_priority_create_dto_instance.to_dict()
# create an instance of SupportTicketPriorityCreateDto from a dict
support_ticket_priority_create_dto_from_dict = SupportTicketPriorityCreateDto.from_dict(support_ticket_priority_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


