# ActivityRecordDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ActivityRecordDto]**](ActivityRecordDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_record_dto_list_envelope import ActivityRecordDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRecordDtoListEnvelope from a JSON string
activity_record_dto_list_envelope_instance = ActivityRecordDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ActivityRecordDtoListEnvelope.to_json())

# convert the object into a dict
activity_record_dto_list_envelope_dict = activity_record_dto_list_envelope_instance.to_dict()
# create an instance of ActivityRecordDtoListEnvelope from a dict
activity_record_dto_list_envelope_from_dict = ActivityRecordDtoListEnvelope.from_dict(activity_record_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


