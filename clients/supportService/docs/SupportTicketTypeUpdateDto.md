# SupportTicketTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_type_update_dto import SupportTicketTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketTypeUpdateDto from a JSON string
support_ticket_type_update_dto_instance = SupportTicketTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketTypeUpdateDto.to_json())

# convert the object into a dict
support_ticket_type_update_dto_dict = support_ticket_type_update_dto_instance.to_dict()
# create an instance of SupportTicketTypeUpdateDto from a dict
support_ticket_type_update_dto_from_dict = SupportTicketTypeUpdateDto.from_dict(support_ticket_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


