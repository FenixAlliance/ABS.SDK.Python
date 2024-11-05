# TaskTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**display_in_time_tracker** | **bool** |  | [optional] 
**requires_description** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.task_type_update_dto import TaskTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeUpdateDto from a JSON string
task_type_update_dto_instance = TaskTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TaskTypeUpdateDto.to_json())

# convert the object into a dict
task_type_update_dto_dict = task_type_update_dto_instance.to_dict()
# create an instance of TaskTypeUpdateDto from a dict
task_type_update_dto_from_dict = TaskTypeUpdateDto.from_dict(task_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


