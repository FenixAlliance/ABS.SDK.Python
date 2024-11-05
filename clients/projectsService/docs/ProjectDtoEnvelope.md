# ProjectDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ProjectDto**](ProjectDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.project_dto_envelope import ProjectDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDtoEnvelope from a JSON string
project_dto_envelope_instance = ProjectDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ProjectDtoEnvelope.to_json())

# convert the object into a dict
project_dto_envelope_dict = project_dto_envelope_instance.to_dict()
# create an instance of ProjectDtoEnvelope from a dict
project_dto_envelope_from_dict = ProjectDtoEnvelope.from_dict(project_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


