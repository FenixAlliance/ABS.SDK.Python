# LeaveTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.leave_type_update_dto import LeaveTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveTypeUpdateDto from a JSON string
leave_type_update_dto_instance = LeaveTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(LeaveTypeUpdateDto.to_json())

# convert the object into a dict
leave_type_update_dto_dict = leave_type_update_dto_instance.to_dict()
# create an instance of LeaveTypeUpdateDto from a dict
leave_type_update_dto_from_dict = LeaveTypeUpdateDto.from_dict(leave_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


