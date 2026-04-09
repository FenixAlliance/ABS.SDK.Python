# TenantPositionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TenantPositionDto**](TenantPositionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_position_dto_envelope import TenantPositionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPositionDtoEnvelope from a JSON string
tenant_position_dto_envelope_instance = TenantPositionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantPositionDtoEnvelope.to_json())

# convert the object into a dict
tenant_position_dto_envelope_dict = tenant_position_dto_envelope_instance.to_dict()
# create an instance of TenantPositionDtoEnvelope from a dict
tenant_position_dto_envelope_from_dict = TenantPositionDtoEnvelope.from_dict(tenant_position_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


