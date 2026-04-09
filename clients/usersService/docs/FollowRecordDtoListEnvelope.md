# FollowRecordDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[FollowRecordDto]**](FollowRecordDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.follow_record_dto_list_envelope import FollowRecordDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FollowRecordDtoListEnvelope from a JSON string
follow_record_dto_list_envelope_instance = FollowRecordDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(FollowRecordDtoListEnvelope.to_json())

# convert the object into a dict
follow_record_dto_list_envelope_dict = follow_record_dto_list_envelope_instance.to_dict()
# create an instance of FollowRecordDtoListEnvelope from a dict
follow_record_dto_list_envelope_from_dict = FollowRecordDtoListEnvelope.from_dict(follow_record_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


