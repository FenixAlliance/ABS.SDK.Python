# SupportTicketTypeDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SupportTicketTypeDto]**](SupportTicketTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.support_ticket_type_dto_list_envelope import SupportTicketTypeDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupportTicketTypeDtoListEnvelope from a JSON string
support_ticket_type_dto_list_envelope_instance = SupportTicketTypeDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupportTicketTypeDtoListEnvelope.to_json())

# convert the object into a dict
support_ticket_type_dto_list_envelope_dict = support_ticket_type_dto_list_envelope_instance.to_dict()
# create an instance of SupportTicketTypeDtoListEnvelope from a dict
support_ticket_type_dto_list_envelope_from_dict = SupportTicketTypeDtoListEnvelope.from_dict(support_ticket_type_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


