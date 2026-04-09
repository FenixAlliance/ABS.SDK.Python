# TenantTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_type_create_dto import TenantTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTypeCreateDto from a JSON string
tenant_type_create_dto_instance = TenantTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTypeCreateDto.to_json())

# convert the object into a dict
tenant_type_create_dto_dict = tenant_type_create_dto_instance.to_dict()
# create an instance of TenantTypeCreateDto from a dict
tenant_type_create_dto_from_dict = TenantTypeCreateDto.from_dict(tenant_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


