# PrivateMessageUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.private_message_update_dto import PrivateMessageUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageUpdateDto from a JSON string
private_message_update_dto_instance = PrivateMessageUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageUpdateDto.to_json())

# convert the object into a dict
private_message_update_dto_dict = private_message_update_dto_instance.to_dict()
# create an instance of PrivateMessageUpdateDto from a dict
private_message_update_dto_from_dict = PrivateMessageUpdateDto.from_dict(private_message_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


