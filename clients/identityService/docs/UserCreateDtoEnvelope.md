# UserCreateDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**UserCreateDto**](UserCreateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_create_dto_envelope import UserCreateDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateDtoEnvelope from a JSON string
user_create_dto_envelope_instance = UserCreateDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserCreateDtoEnvelope.to_json())

# convert the object into a dict
user_create_dto_envelope_dict = user_create_dto_envelope_instance.to_dict()
# create an instance of UserCreateDtoEnvelope from a dict
user_create_dto_envelope_from_dict = UserCreateDtoEnvelope.from_dict(user_create_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


