# LeaveApplicationUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**justification** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**on_review** | **bool** |  | [optional] 
**leave_type_id** | **str** |  | [optional] 
**employee_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.leave_application_update_dto import LeaveApplicationUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveApplicationUpdateDto from a JSON string
leave_application_update_dto_instance = LeaveApplicationUpdateDto.from_json(json)
# print the JSON string representation of the object
print(LeaveApplicationUpdateDto.to_json())

# convert the object into a dict
leave_application_update_dto_dict = leave_application_update_dto_instance.to_dict()
# create an instance of LeaveApplicationUpdateDto from a dict
leave_application_update_dto_from_dict = LeaveApplicationUpdateDto.from_dict(leave_application_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


