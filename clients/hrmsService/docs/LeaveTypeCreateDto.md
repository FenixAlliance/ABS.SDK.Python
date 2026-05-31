# LeaveTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.leave_type_create_dto import LeaveTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveTypeCreateDto from a JSON string
leave_type_create_dto_instance = LeaveTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(LeaveTypeCreateDto.to_json())

# convert the object into a dict
leave_type_create_dto_dict = leave_type_create_dto_instance.to_dict()
# create an instance of LeaveTypeCreateDto from a dict
leave_type_create_dto_from_dict = LeaveTypeCreateDto.from_dict(leave_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


