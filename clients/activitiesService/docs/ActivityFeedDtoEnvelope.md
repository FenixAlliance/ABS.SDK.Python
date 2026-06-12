# ActivityFeedDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ActivityFeedDto**](ActivityFeedDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.activity_feed_dto_envelope import ActivityFeedDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityFeedDtoEnvelope from a JSON string
activity_feed_dto_envelope_instance = ActivityFeedDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ActivityFeedDtoEnvelope.to_json())

# convert the object into a dict
activity_feed_dto_envelope_dict = activity_feed_dto_envelope_instance.to_dict()
# create an instance of ActivityFeedDtoEnvelope from a dict
activity_feed_dto_envelope_from_dict = ActivityFeedDtoEnvelope.from_dict(activity_feed_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


