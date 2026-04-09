# ProjectPeriodDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ProjectPeriodDto]**](ProjectPeriodDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.project_period_dto_list_envelope import ProjectPeriodDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPeriodDtoListEnvelope from a JSON string
project_period_dto_list_envelope_instance = ProjectPeriodDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ProjectPeriodDtoListEnvelope.to_json())

# convert the object into a dict
project_period_dto_list_envelope_dict = project_period_dto_list_envelope_instance.to_dict()
# create an instance of ProjectPeriodDtoListEnvelope from a dict
project_period_dto_list_envelope_from_dict = ProjectPeriodDtoListEnvelope.from_dict(project_period_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


