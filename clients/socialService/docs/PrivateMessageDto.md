# PrivateMessageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**read** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**conversation_id** | **str** |  | [optional] 
**sender_social_profile_id** | **str** |  | [optional] 
**receiver_social_profile_id** | **str** |  | [optional] 
**sent_timestamp** | **datetime** |  | [optional] 
**read_timestamp** | **datetime** |  | [optional] 
**received_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.private_message_dto import PrivateMessageDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageDto from a JSON string
private_message_dto_instance = PrivateMessageDto.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageDto.to_json())

# convert the object into a dict
private_message_dto_dict = private_message_dto_instance.to_dict()
# create an instance of PrivateMessageDto from a dict
private_message_dto_from_dict = PrivateMessageDto.from_dict(private_message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


