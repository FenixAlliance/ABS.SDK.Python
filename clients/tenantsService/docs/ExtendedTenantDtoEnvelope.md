# ExtendedTenantDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ExtendedTenantDto**](ExtendedTenantDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_tenant_dto_envelope import ExtendedTenantDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedTenantDtoEnvelope from a JSON string
extended_tenant_dto_envelope_instance = ExtendedTenantDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExtendedTenantDtoEnvelope.to_json())

# convert the object into a dict
extended_tenant_dto_envelope_dict = extended_tenant_dto_envelope_instance.to_dict()
# create an instance of ExtendedTenantDtoEnvelope from a dict
extended_tenant_dto_envelope_from_dict = ExtendedTenantDtoEnvelope.from_dict(extended_tenant_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


