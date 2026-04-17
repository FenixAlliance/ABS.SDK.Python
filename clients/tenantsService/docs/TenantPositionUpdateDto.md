# TenantPositionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_position_update_dto import TenantPositionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPositionUpdateDto from a JSON string
tenant_position_update_dto_instance = TenantPositionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantPositionUpdateDto.to_json())

# convert the object into a dict
tenant_position_update_dto_dict = tenant_position_update_dto_instance.to_dict()
# create an instance of TenantPositionUpdateDto from a dict
tenant_position_update_dto_from_dict = TenantPositionUpdateDto.from_dict(tenant_position_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


