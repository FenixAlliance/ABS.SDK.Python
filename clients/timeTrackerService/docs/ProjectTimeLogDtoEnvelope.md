# ProjectTimeLogDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ProjectTimeLogDto**](ProjectTimeLogDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.project_time_log_dto_envelope import ProjectTimeLogDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTimeLogDtoEnvelope from a JSON string
project_time_log_dto_envelope_instance = ProjectTimeLogDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ProjectTimeLogDtoEnvelope.to_json())

# convert the object into a dict
project_time_log_dto_envelope_dict = project_time_log_dto_envelope_instance.to_dict()
# create an instance of ProjectTimeLogDtoEnvelope from a dict
project_time_log_dto_envelope_from_dict = ProjectTimeLogDtoEnvelope.from_dict(project_time_log_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


