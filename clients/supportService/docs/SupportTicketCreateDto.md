# SupportTicketCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**support_ticket_type_id** | **str** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**support_priority_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_create_dto import SupportTicketCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketCreateDto from a JSON string
support_ticket_create_dto_instance = SupportTicketCreateDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketCreateDto.to_json())

# convert the object into a dict
support_ticket_create_dto_dict = support_ticket_create_dto_instance.to_dict()
# create an instance of SupportTicketCreateDto from a dict
support_ticket_create_dto_from_dict = SupportTicketCreateDto.from_dict(support_ticket_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


