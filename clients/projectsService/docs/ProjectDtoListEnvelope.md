# ProjectDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ProjectDto]**](ProjectDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.project_dto_list_envelope import ProjectDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDtoListEnvelope from a JSON string
project_dto_list_envelope_instance = ProjectDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ProjectDtoListEnvelope.to_json())

# convert the object into a dict
project_dto_list_envelope_dict = project_dto_list_envelope_instance.to_dict()
# create an instance of ProjectDtoListEnvelope from a dict
project_dto_list_envelope_from_dict = ProjectDtoListEnvelope.from_dict(project_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


