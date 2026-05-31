# LeaveTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.leave_type_dto import LeaveTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveTypeDto from a JSON string
leave_type_dto_instance = LeaveTypeDto.from_json(json)
# print the JSON string representation of the object
print(LeaveTypeDto.to_json())

# convert the object into a dict
leave_type_dto_dict = leave_type_dto_instance.to_dict()
# create an instance of LeaveTypeDto from a dict
leave_type_dto_from_dict = LeaveTypeDto.from_dict(leave_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


