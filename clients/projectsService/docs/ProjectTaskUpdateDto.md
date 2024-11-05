# ProjectTaskUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | [optional] 
**due_line** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.project_task_update_dto import ProjectTaskUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTaskUpdateDto from a JSON string
project_task_update_dto_instance = ProjectTaskUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectTaskUpdateDto.to_json())

# convert the object into a dict
project_task_update_dto_dict = project_task_update_dto_instance.to_dict()
# create an instance of ProjectTaskUpdateDto from a dict
project_task_update_dto_from_dict = ProjectTaskUpdateDto.from_dict(project_task_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


