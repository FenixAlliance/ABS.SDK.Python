# ExtendedTenantEnrolmentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ExtendedTenantEnrolmentDto]**](ExtendedTenantEnrolmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_tenant_enrolment_dto_list_envelope import ExtendedTenantEnrolmentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedTenantEnrolmentDtoListEnvelope from a JSON string
extended_tenant_enrolment_dto_list_envelope_instance = ExtendedTenantEnrolmentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExtendedTenantEnrolmentDtoListEnvelope.to_json())

# convert the object into a dict
extended_tenant_enrolment_dto_list_envelope_dict = extended_tenant_enrolment_dto_list_envelope_instance.to_dict()
# create an instance of ExtendedTenantEnrolmentDtoListEnvelope from a dict
extended_tenant_enrolment_dto_list_envelope_from_dict = ExtendedTenantEnrolmentDtoListEnvelope.from_dict(extended_tenant_enrolment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


