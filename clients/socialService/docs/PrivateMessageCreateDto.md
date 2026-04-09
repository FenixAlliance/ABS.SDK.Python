# PrivateMessageCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**conversation_id** | **str** |  | [optional] 
**sender_social_profile_id** | **str** |  | [optional] 
**receiver_social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.private_message_create_dto import PrivateMessageCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageCreateDto from a JSON string
private_message_create_dto_instance = PrivateMessageCreateDto.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageCreateDto.to_json())

# convert the object into a dict
private_message_create_dto_dict = private_message_create_dto_instance.to_dict()
# create an instance of PrivateMessageCreateDto from a dict
private_message_create_dto_from_dict = PrivateMessageCreateDto.from_dict(private_message_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


