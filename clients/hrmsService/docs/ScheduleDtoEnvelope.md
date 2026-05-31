# ScheduleDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ScheduleDto**](ScheduleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_dto_envelope import ScheduleDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDtoEnvelope from a JSON string
schedule_dto_envelope_instance = ScheduleDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ScheduleDtoEnvelope.to_json())

# convert the object into a dict
schedule_dto_envelope_dict = schedule_dto_envelope_instance.to_dict()
# create an instance of ScheduleDtoEnvelope from a dict
schedule_dto_envelope_from_dict = ScheduleDtoEnvelope.from_dict(schedule_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


