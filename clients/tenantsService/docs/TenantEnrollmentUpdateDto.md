# TenantEnrollmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_admin** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_enrollment_update_dto import TenantEnrollmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantEnrollmentUpdateDto from a JSON string
tenant_enrollment_update_dto_instance = TenantEnrollmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantEnrollmentUpdateDto.to_json())

# convert the object into a dict
tenant_enrollment_update_dto_dict = tenant_enrollment_update_dto_instance.to_dict()
# create an instance of TenantEnrollmentUpdateDto from a dict
tenant_enrollment_update_dto_from_dict = TenantEnrollmentUpdateDto.from_dict(tenant_enrollment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


