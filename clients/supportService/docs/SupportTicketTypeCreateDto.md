# SupportTicketTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_type_create_dto import SupportTicketTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketTypeCreateDto from a JSON string
support_ticket_type_create_dto_instance = SupportTicketTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(SupportTicketTypeCreateDto.to_json())

# convert the object into a dict
support_ticket_type_create_dto_dict = support_ticket_type_create_dto_instance.to_dict()
# create an instance of SupportTicketTypeCreateDto from a dict
support_ticket_type_create_dto_from_dict = SupportTicketTypeCreateDto.from_dict(support_ticket_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


