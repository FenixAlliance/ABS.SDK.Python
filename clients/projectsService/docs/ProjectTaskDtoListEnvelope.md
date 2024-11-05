# ProjectTaskDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ProjectTaskDto]**](ProjectTaskDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.project_task_dto_list_envelope import ProjectTaskDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTaskDtoListEnvelope from a JSON string
project_task_dto_list_envelope_instance = ProjectTaskDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ProjectTaskDtoListEnvelope.to_json())

# convert the object into a dict
project_task_dto_list_envelope_dict = project_task_dto_list_envelope_instance.to_dict()
# create an instance of ProjectTaskDtoListEnvelope from a dict
project_task_dto_list_envelope_from_dict = ProjectTaskDtoListEnvelope.from_dict(project_task_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


