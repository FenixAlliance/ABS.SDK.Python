# SimpleTenantEnrolmentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.simple_tenant_enrolment_dto import SimpleTenantEnrolmentDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleTenantEnrolmentDto from a JSON string
simple_tenant_enrolment_dto_instance = SimpleTenantEnrolmentDto.from_json(json)
# print the JSON string representation of the object
print(SimpleTenantEnrolmentDto.to_json())

# convert the object into a dict
simple_tenant_enrolment_dto_dict = simple_tenant_enrolment_dto_instance.to_dict()
# create an instance of SimpleTenantEnrolmentDto from a dict
simple_tenant_enrolment_dto_from_dict = SimpleTenantEnrolmentDto.from_dict(simple_tenant_enrolment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


