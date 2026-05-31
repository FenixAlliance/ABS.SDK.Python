# LeaveApplicationDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LeaveApplicationDto]**](LeaveApplicationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.leave_application_dto_list_envelope import LeaveApplicationDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveApplicationDtoListEnvelope from a JSON string
leave_application_dto_list_envelope_instance = LeaveApplicationDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LeaveApplicationDtoListEnvelope.to_json())

# convert the object into a dict
leave_application_dto_list_envelope_dict = leave_application_dto_list_envelope_instance.to_dict()
# create an instance of LeaveApplicationDtoListEnvelope from a dict
leave_application_dto_list_envelope_from_dict = LeaveApplicationDtoListEnvelope.from_dict(leave_application_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


