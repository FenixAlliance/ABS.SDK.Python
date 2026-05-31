# TimeIntervalDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TimeIntervalDto]**](TimeIntervalDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.time_interval_dto_list_envelope import TimeIntervalDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TimeIntervalDtoListEnvelope from a JSON string
time_interval_dto_list_envelope_instance = TimeIntervalDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TimeIntervalDtoListEnvelope.to_json())

# convert the object into a dict
time_interval_dto_list_envelope_dict = time_interval_dto_list_envelope_instance.to_dict()
# create an instance of TimeIntervalDtoListEnvelope from a dict
time_interval_dto_list_envelope_from_dict = TimeIntervalDtoListEnvelope.from_dict(time_interval_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


