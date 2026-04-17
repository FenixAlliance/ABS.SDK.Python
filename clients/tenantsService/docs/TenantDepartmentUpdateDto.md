# TenantDepartmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**organization_profile_id** | **str** |  | [optional] 
**parent_department_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_department_update_dto import TenantDepartmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDepartmentUpdateDto from a JSON string
tenant_department_update_dto_instance = TenantDepartmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantDepartmentUpdateDto.to_json())

# convert the object into a dict
tenant_department_update_dto_dict = tenant_department_update_dto_instance.to_dict()
# create an instance of TenantDepartmentUpdateDto from a dict
tenant_department_update_dto_from_dict = TenantDepartmentUpdateDto.from_dict(tenant_department_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


