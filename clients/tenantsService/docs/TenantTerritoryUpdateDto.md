# TenantTerritoryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_territory_update_dto import TenantTerritoryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTerritoryUpdateDto from a JSON string
tenant_territory_update_dto_instance = TenantTerritoryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTerritoryUpdateDto.to_json())

# convert the object into a dict
tenant_territory_update_dto_dict = tenant_territory_update_dto_instance.to_dict()
# create an instance of TenantTerritoryUpdateDto from a dict
tenant_territory_update_dto_from_dict = TenantTerritoryUpdateDto.from_dict(tenant_territory_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


