# NotificationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**read** | **bool** |  | [optional] 
**icon** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**read_timestamp** | **datetime** |  | [optional] 
**issued_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.notification_dto import NotificationDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDto from a JSON string
notification_dto_instance = NotificationDto.from_json(json)
# print the JSON string representation of the object
print(NotificationDto.to_json())

# convert the object into a dict
notification_dto_dict = notification_dto_instance.to_dict()
# create an instance of NotificationDto from a dict
notification_dto_from_dict = NotificationDto.from_dict(notification_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


