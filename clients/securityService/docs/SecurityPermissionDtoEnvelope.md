# SecurityPermissionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SecurityPermissionDto**](SecurityPermissionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.security_permission_dto_envelope import SecurityPermissionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPermissionDtoEnvelope from a JSON string
security_permission_dto_envelope_instance = SecurityPermissionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SecurityPermissionDtoEnvelope.to_json())

# convert the object into a dict
security_permission_dto_envelope_dict = security_permission_dto_envelope_instance.to_dict()
# create an instance of SecurityPermissionDtoEnvelope from a dict
security_permission_dto_envelope_from_dict = SecurityPermissionDtoEnvelope.from_dict(security_permission_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


