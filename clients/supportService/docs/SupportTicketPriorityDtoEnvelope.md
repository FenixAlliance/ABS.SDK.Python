# SupportTicketPriorityDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SupportTicketPriorityDto**](SupportTicketPriorityDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_priority_dto_envelope import SupportTicketPriorityDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketPriorityDtoEnvelope from a JSON string
support_ticket_priority_dto_envelope_instance = SupportTicketPriorityDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupportTicketPriorityDtoEnvelope.to_json())

# convert the object into a dict
support_ticket_priority_dto_envelope_dict = support_ticket_priority_dto_envelope_instance.to_dict()
# create an instance of SupportTicketPriorityDtoEnvelope from a dict
support_ticket_priority_dto_envelope_from_dict = SupportTicketPriorityDtoEnvelope.from_dict(support_ticket_priority_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


