# LeaveApplicationCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**justification** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**on_review** | **bool** |  | [optional] 
**leave_type_id** | **str** |  | 
**employee_profile_id** | **str** |  | 

## Example

```python
from openapi_client.models.leave_application_create_dto import LeaveApplicationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveApplicationCreateDto from a JSON string
leave_application_create_dto_instance = LeaveApplicationCreateDto.from_json(json)
# print the JSON string representation of the object
print(LeaveApplicationCreateDto.to_json())

# convert the object into a dict
leave_application_create_dto_dict = leave_application_create_dto_instance.to_dict()
# create an instance of LeaveApplicationCreateDto from a dict
leave_application_create_dto_from_dict = LeaveApplicationCreateDto.from_dict(leave_application_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


