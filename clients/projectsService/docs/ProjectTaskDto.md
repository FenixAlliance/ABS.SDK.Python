# ProjectTaskDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**due_line** | **datetime** |  | [optional] 
**project_id** | **str** |  | [optional] 
**project_task_bucket_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_task_dto import ProjectTaskDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTaskDto from a JSON string
project_task_dto_instance = ProjectTaskDto.from_json(json)
# print the JSON string representation of the object
print(ProjectTaskDto.to_json())

# convert the object into a dict
project_task_dto_dict = project_task_dto_instance.to_dict()
# create an instance of ProjectTaskDto from a dict
project_task_dto_from_dict = ProjectTaskDto.from_dict(project_task_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


