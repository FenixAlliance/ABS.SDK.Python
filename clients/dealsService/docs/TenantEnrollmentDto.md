# TenantEnrollmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**is_root** | **bool** |  | [optional] 
**is_owner** | **bool** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_enrollment_dto import TenantEnrollmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantEnrollmentDto from a JSON string
tenant_enrollment_dto_instance = TenantEnrollmentDto.from_json(json)
# print the JSON string representation of the object
print(TenantEnrollmentDto.to_json())

# convert the object into a dict
tenant_enrollment_dto_dict = tenant_enrollment_dto_instance.to_dict()
# create an instance of TenantEnrollmentDto from a dict
tenant_enrollment_dto_from_dict = TenantEnrollmentDto.from_dict(tenant_enrollment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


