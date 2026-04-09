# TenantDepartmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**organization_profile_id** | **str** |  | [optional] 
**parent_department_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_department_dto import TenantDepartmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDepartmentDto from a JSON string
tenant_department_dto_instance = TenantDepartmentDto.from_json(json)
# print the JSON string representation of the object
print(TenantDepartmentDto.to_json())

# convert the object into a dict
tenant_department_dto_dict = tenant_department_dto_instance.to_dict()
# create an instance of TenantDepartmentDto from a dict
tenant_department_dto_from_dict = TenantDepartmentDto.from_dict(tenant_department_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


