# ConversationCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**subject** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.conversation_create_dto import ConversationCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationCreateDto from a JSON string
conversation_create_dto_instance = ConversationCreateDto.from_json(json)
# print the JSON string representation of the object
print(ConversationCreateDto.to_json())

# convert the object into a dict
conversation_create_dto_dict = conversation_create_dto_instance.to_dict()
# create an instance of ConversationCreateDto from a dict
conversation_create_dto_from_dict = ConversationCreateDto.from_dict(conversation_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


