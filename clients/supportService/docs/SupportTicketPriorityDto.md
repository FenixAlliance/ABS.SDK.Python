# SupportTicketPriorityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_priority_dto import SupportTicketPriorityDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketPriorityDto from a JSON string
support_ticket_priority_dto_instance = SupportTicketPriorityDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketPriorityDto.to_json())

# convert the object into a dict
support_ticket_priority_dto_dict = support_ticket_priority_dto_instance.to_dict()
# create an instance of SupportTicketPriorityDto from a dict
support_ticket_priority_dto_from_dict = SupportTicketPriorityDto.from_dict(support_ticket_priority_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


