# ExtendedTenantEnrolmentDto


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
**tenant** | [**TenantDto**](TenantDto.md) |  | [optional] 
**user** | [**UserDto**](UserDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_tenant_enrolment_dto import ExtendedTenantEnrolmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedTenantEnrolmentDto from a JSON string
extended_tenant_enrolment_dto_instance = ExtendedTenantEnrolmentDto.from_json(json)
# print the JSON string representation of the object
print(ExtendedTenantEnrolmentDto.to_json())

# convert the object into a dict
extended_tenant_enrolment_dto_dict = extended_tenant_enrolment_dto_instance.to_dict()
# create an instance of ExtendedTenantEnrolmentDto from a dict
extended_tenant_enrolment_dto_from_dict = ExtendedTenantEnrolmentDto.from_dict(extended_tenant_enrolment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


