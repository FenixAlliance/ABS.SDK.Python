# ProjectTimeLogDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ProjectTimeLogDto]**](ProjectTimeLogDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.project_time_log_dto_list_envelope import ProjectTimeLogDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTimeLogDtoListEnvelope from a JSON string
project_time_log_dto_list_envelope_instance = ProjectTimeLogDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ProjectTimeLogDtoListEnvelope.to_json())

# convert the object into a dict
project_time_log_dto_list_envelope_dict = project_time_log_dto_list_envelope_instance.to_dict()
# create an instance of ProjectTimeLogDtoListEnvelope from a dict
project_time_log_dto_list_envelope_from_dict = ProjectTimeLogDtoListEnvelope.from_dict(project_time_log_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


