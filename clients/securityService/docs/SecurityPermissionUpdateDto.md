# SecurityPermissionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.security_permission_update_dto import SecurityPermissionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPermissionUpdateDto from a JSON string
security_permission_update_dto_instance = SecurityPermissionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SecurityPermissionUpdateDto.to_json())

# convert the object into a dict
security_permission_update_dto_dict = security_permission_update_dto_instance.to_dict()
# create an instance of SecurityPermissionUpdateDto from a dict
security_permission_update_dto_from_dict = SecurityPermissionUpdateDto.from_dict(security_permission_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


