# NotificationDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**NotificationDto**](NotificationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.notification_dto_envelope import NotificationDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDtoEnvelope from a JSON string
notification_dto_envelope_instance = NotificationDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(NotificationDtoEnvelope.to_json())

# convert the object into a dict
notification_dto_envelope_dict = notification_dto_envelope_instance.to_dict()
# create an instance of NotificationDtoEnvelope from a dict
notification_dto_envelope_from_dict = NotificationDtoEnvelope.from_dict(notification_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


