# TimezoneDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TimezoneDto]**](TimezoneDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.timezone_dto_list_envelope import TimezoneDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneDtoListEnvelope from a JSON string
timezone_dto_list_envelope_instance = TimezoneDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TimezoneDtoListEnvelope.to_json())

# convert the object into a dict
timezone_dto_list_envelope_dict = timezone_dto_list_envelope_instance.to_dict()
# create an instance of TimezoneDtoListEnvelope from a dict
timezone_dto_list_envelope_from_dict = TimezoneDtoListEnvelope.from_dict(timezone_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


