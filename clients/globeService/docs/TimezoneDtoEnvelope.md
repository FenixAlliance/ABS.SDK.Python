# TimezoneDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TimezoneDto**](TimezoneDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.timezone_dto_envelope import TimezoneDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneDtoEnvelope from a JSON string
timezone_dto_envelope_instance = TimezoneDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TimezoneDtoEnvelope.to_json())

# convert the object into a dict
timezone_dto_envelope_dict = timezone_dto_envelope_instance.to_dict()
# create an instance of TimezoneDtoEnvelope from a dict
timezone_dto_envelope_from_dict = TimezoneDtoEnvelope.from_dict(timezone_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


