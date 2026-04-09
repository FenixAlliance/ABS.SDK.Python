# ExtendedTenantEnrollmentDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ExtendedTenantEnrollmentDto**](ExtendedTenantEnrollmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_tenant_enrollment_dto_envelope import ExtendedTenantEnrollmentDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedTenantEnrollmentDtoEnvelope from a JSON string
extended_tenant_enrollment_dto_envelope_instance = ExtendedTenantEnrollmentDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExtendedTenantEnrollmentDtoEnvelope.to_json())

# convert the object into a dict
extended_tenant_enrollment_dto_envelope_dict = extended_tenant_enrollment_dto_envelope_instance.to_dict()
# create an instance of ExtendedTenantEnrollmentDtoEnvelope from a dict
extended_tenant_enrollment_dto_envelope_from_dict = ExtendedTenantEnrollmentDtoEnvelope.from_dict(extended_tenant_enrollment_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


