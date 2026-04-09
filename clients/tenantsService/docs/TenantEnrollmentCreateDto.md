# TenantEnrollmentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_enrollment_create_dto import TenantEnrollmentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantEnrollmentCreateDto from a JSON string
tenant_enrollment_create_dto_instance = TenantEnrollmentCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantEnrollmentCreateDto.to_json())

# convert the object into a dict
tenant_enrollment_create_dto_dict = tenant_enrollment_create_dto_instance.to_dict()
# create an instance of TenantEnrollmentCreateDto from a dict
tenant_enrollment_create_dto_from_dict = TenantEnrollmentCreateDto.from_dict(tenant_enrollment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


