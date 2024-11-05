# SupportTicketTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_type_dto import SupportTicketTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketTypeDto from a JSON string
support_ticket_type_dto_instance = SupportTicketTypeDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketTypeDto.to_json())

# convert the object into a dict
support_ticket_type_dto_dict = support_ticket_type_dto_instance.to_dict()
# create an instance of SupportTicketTypeDto from a dict
support_ticket_type_dto_from_dict = SupportTicketTypeDto.from_dict(support_ticket_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


