# ActivityRecordDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ActivityRecordDto**](ActivityRecordDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_record_dto_envelope import ActivityRecordDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRecordDtoEnvelope from a JSON string
activity_record_dto_envelope_instance = ActivityRecordDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ActivityRecordDtoEnvelope.to_json())

# convert the object into a dict
activity_record_dto_envelope_dict = activity_record_dto_envelope_instance.to_dict()
# create an instance of ActivityRecordDtoEnvelope from a dict
activity_record_dto_envelope_from_dict = ActivityRecordDtoEnvelope.from_dict(activity_record_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


