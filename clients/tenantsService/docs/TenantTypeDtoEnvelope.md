# TenantTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TenantTypeDto**](TenantTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_type_dto_envelope import TenantTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTypeDtoEnvelope from a JSON string
tenant_type_dto_envelope_instance = TenantTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantTypeDtoEnvelope.to_json())

# convert the object into a dict
tenant_type_dto_envelope_dict = tenant_type_dto_envelope_instance.to_dict()
# create an instance of TenantTypeDtoEnvelope from a dict
tenant_type_dto_envelope_from_dict = TenantTypeDtoEnvelope.from_dict(tenant_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


