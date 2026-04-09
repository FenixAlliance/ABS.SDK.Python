# TenantTerritoryDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TenantTerritoryDto**](TenantTerritoryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_territory_dto_envelope import TenantTerritoryDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTerritoryDtoEnvelope from a JSON string
tenant_territory_dto_envelope_instance = TenantTerritoryDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantTerritoryDtoEnvelope.to_json())

# convert the object into a dict
tenant_territory_dto_envelope_dict = tenant_territory_dto_envelope_instance.to_dict()
# create an instance of TenantTerritoryDtoEnvelope from a dict
tenant_territory_dto_envelope_from_dict = TenantTerritoryDtoEnvelope.from_dict(tenant_territory_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


