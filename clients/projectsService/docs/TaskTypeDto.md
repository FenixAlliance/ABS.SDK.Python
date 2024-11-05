# TaskTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**task_category_id** | **str** |  | [optional] 
**display_in_time_tracker** | **bool** |  | [optional] 
**requires_description** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.task_type_dto import TaskTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeDto from a JSON string
task_type_dto_instance = TaskTypeDto.from_json(json)
# print the JSON string representation of the object
print(TaskTypeDto.to_json())

# convert the object into a dict
task_type_dto_dict = task_type_dto_instance.to_dict()
# create an instance of TaskTypeDto from a dict
task_type_dto_from_dict = TaskTypeDto.from_dict(task_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


