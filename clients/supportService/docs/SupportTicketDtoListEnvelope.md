# SupportTicketDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SupportTicketDto]**](SupportTicketDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_dto_list_envelope import SupportTicketDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketDtoListEnvelope from a JSON string
support_ticket_dto_list_envelope_instance = SupportTicketDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupportTicketDtoListEnvelope.to_json())

# convert the object into a dict
support_ticket_dto_list_envelope_dict = support_ticket_dto_list_envelope_instance.to_dict()
# create an instance of SupportTicketDtoListEnvelope from a dict
support_ticket_dto_list_envelope_from_dict = SupportTicketDtoListEnvelope.from_dict(support_ticket_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


