# LeaveTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**LeaveTypeDto**](LeaveTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.leave_type_dto_envelope import LeaveTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveTypeDtoEnvelope from a JSON string
leave_type_dto_envelope_instance = LeaveTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(LeaveTypeDtoEnvelope.to_json())

# convert the object into a dict
leave_type_dto_envelope_dict = leave_type_dto_envelope_instance.to_dict()
# create an instance of LeaveTypeDtoEnvelope from a dict
leave_type_dto_envelope_from_dict = LeaveTypeDtoEnvelope.from_dict(leave_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


