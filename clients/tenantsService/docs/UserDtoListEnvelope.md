# UserDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[UserDto]**](UserDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_dto_list_envelope import UserDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserDtoListEnvelope from a JSON string
user_dto_list_envelope_instance = UserDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserDtoListEnvelope.to_json())

# convert the object into a dict
user_dto_list_envelope_dict = user_dto_list_envelope_instance.to_dict()
# create an instance of UserDtoListEnvelope from a dict
user_dto_list_envelope_from_dict = UserDtoListEnvelope.from_dict(user_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


