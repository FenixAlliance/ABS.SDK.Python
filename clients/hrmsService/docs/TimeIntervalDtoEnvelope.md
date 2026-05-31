# TimeIntervalDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TimeIntervalDto**](TimeIntervalDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.time_interval_dto_envelope import TimeIntervalDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TimeIntervalDtoEnvelope from a JSON string
time_interval_dto_envelope_instance = TimeIntervalDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TimeIntervalDtoEnvelope.to_json())

# convert the object into a dict
time_interval_dto_envelope_dict = time_interval_dto_envelope_instance.to_dict()
# create an instance of TimeIntervalDtoEnvelope from a dict
time_interval_dto_envelope_from_dict = TimeIntervalDtoEnvelope.from_dict(time_interval_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


