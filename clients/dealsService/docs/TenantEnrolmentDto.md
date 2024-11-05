# TenantEnrolmentDto


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
from openapi_client.models.tenant_enrolment_dto import TenantEnrolmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantEnrolmentDto from a JSON string
tenant_enrolment_dto_instance = TenantEnrolmentDto.from_json(json)
# print the JSON string representation of the object
print(TenantEnrolmentDto.to_json())

# convert the object into a dict
tenant_enrolment_dto_dict = tenant_enrolment_dto_instance.to_dict()
# create an instance of TenantEnrolmentDto from a dict
tenant_enrolment_dto_from_dict = TenantEnrolmentDto.from_dict(tenant_enrolment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


