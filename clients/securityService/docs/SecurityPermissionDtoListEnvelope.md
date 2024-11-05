# SecurityPermissionDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[SecurityPermissionDto]**](SecurityPermissionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.security_permission_dto_list_envelope import SecurityPermissionDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPermissionDtoListEnvelope from a JSON string
security_permission_dto_list_envelope_instance = SecurityPermissionDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(SecurityPermissionDtoListEnvelope.to_json())

# convert the object into a dict
security_permission_dto_list_envelope_dict = security_permission_dto_list_envelope_instance.to_dict()
# create an instance of SecurityPermissionDtoListEnvelope from a dict
security_permission_dto_list_envelope_from_dict = SecurityPermissionDtoListEnvelope.from_dict(security_permission_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


