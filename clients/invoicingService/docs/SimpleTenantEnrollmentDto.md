# SimpleTenantEnrollmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.simple_tenant_enrollment_dto import SimpleTenantEnrollmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTenantEnrollmentDto from a JSON string
simple_tenant_enrollment_dto_instance = SimpleTenantEnrollmentDto.from_json(json)
# print the JSON string representation of the object
print(SimpleTenantEnrollmentDto.to_json())

# convert the object into a dict
simple_tenant_enrollment_dto_dict = simple_tenant_enrollment_dto_instance.to_dict()
# create an instance of SimpleTenantEnrollmentDto from a dict
simple_tenant_enrollment_dto_from_dict = SimpleTenantEnrollmentDto.from_dict(simple_tenant_enrollment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


