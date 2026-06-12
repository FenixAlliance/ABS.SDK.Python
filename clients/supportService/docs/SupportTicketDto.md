# SupportTicketDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**support_ticket_status** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**support_ticket_type_id** | **str** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**support_priority_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_dto import SupportTicketDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketDto from a JSON string
support_ticket_dto_instance = SupportTicketDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketDto.to_json())

# convert the object into a dict
support_ticket_dto_dict = support_ticket_dto_instance.to_dict()
# create an instance of SupportTicketDto from a dict
support_ticket_dto_from_dict = SupportTicketDto.from_dict(support_ticket_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


