# ProjectTaskCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**due_line** | **datetime** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_task_create_dto import ProjectTaskCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTaskCreateDto from a JSON string
project_task_create_dto_instance = ProjectTaskCreateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectTaskCreateDto.to_json())

# convert the object into a dict
project_task_create_dto_dict = project_task_create_dto_instance.to_dict()
# create an instance of ProjectTaskCreateDto from a dict
project_task_create_dto_from_dict = ProjectTaskCreateDto.from_dict(project_task_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


