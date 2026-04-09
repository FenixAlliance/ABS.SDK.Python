# ConversationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**subject** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**started_timestamp** | **datetime** |  | [optional] 
**last_message_timestamp** | **datetime** |  | [optional] 
**last_message** | **str** |  | [optional] 
**social_profile_name** | **str** |  | [optional] 
**social_profile_avatar_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.conversation_dto import ConversationDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationDto from a JSON string
conversation_dto_instance = ConversationDto.from_json(json)
# print the JSON string representation of the object
print(ConversationDto.to_json())

# convert the object into a dict
conversation_dto_dict = conversation_dto_instance.to_dict()
# create an instance of ConversationDto from a dict
conversation_dto_from_dict = ConversationDto.from_dict(conversation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


