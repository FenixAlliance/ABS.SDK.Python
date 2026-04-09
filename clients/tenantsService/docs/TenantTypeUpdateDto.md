# TenantTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_type_update_dto import TenantTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTypeUpdateDto from a JSON string
tenant_type_update_dto_instance = TenantTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTypeUpdateDto.to_json())

# convert the object into a dict
tenant_type_update_dto_dict = tenant_type_update_dto_instance.to_dict()
# create an instance of TenantTypeUpdateDto from a dict
tenant_type_update_dto_from_dict = TenantTypeUpdateDto.from_dict(tenant_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


