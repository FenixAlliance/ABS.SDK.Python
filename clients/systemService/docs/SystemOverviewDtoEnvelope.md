# SystemOverviewDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SystemOverviewDto**](SystemOverviewDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.system_overview_dto_envelope import SystemOverviewDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SystemOverviewDtoEnvelope from a JSON string
system_overview_dto_envelope_instance = SystemOverviewDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SystemOverviewDtoEnvelope.to_json())

# convert the object into a dict
system_overview_dto_envelope_dict = system_overview_dto_envelope_instance.to_dict()
# create an instance of SystemOverviewDtoEnvelope from a dict
system_overview_dto_envelope_from_dict = SystemOverviewDtoEnvelope.from_dict(system_overview_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


