# PrivateMessageDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PrivateMessageDto]**](PrivateMessageDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.private_message_dto_list_envelope import PrivateMessageDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateMessageDtoListEnvelope from a JSON string
private_message_dto_list_envelope_instance = PrivateMessageDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PrivateMessageDtoListEnvelope.to_json())

# convert the object into a dict
private_message_dto_list_envelope_dict = private_message_dto_list_envelope_instance.to_dict()
# create an instance of PrivateMessageDtoListEnvelope from a dict
private_message_dto_list_envelope_from_dict = PrivateMessageDtoListEnvelope.from_dict(private_message_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


