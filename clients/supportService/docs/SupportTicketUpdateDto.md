# SupportTicketUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**support_ticket_type_id** | **str** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**support_priority_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_update_dto import SupportTicketUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketUpdateDto from a JSON string
support_ticket_update_dto_instance = SupportTicketUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketUpdateDto.to_json())

# convert the object into a dict
support_ticket_update_dto_dict = support_ticket_update_dto_instance.to_dict()
# create an instance of SupportTicketUpdateDto from a dict
support_ticket_update_dto_from_dict = SupportTicketUpdateDto.from_dict(support_ticket_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


