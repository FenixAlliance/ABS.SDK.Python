# TenantTerritoryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parent_territory_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_territory_create_dto import TenantTerritoryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTerritoryCreateDto from a JSON string
tenant_territory_create_dto_instance = TenantTerritoryCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTerritoryCreateDto.to_json())

# convert the object into a dict
tenant_territory_create_dto_dict = tenant_territory_create_dto_instance.to_dict()
# create an instance of TenantTerritoryCreateDto from a dict
tenant_territory_create_dto_from_dict = TenantTerritoryCreateDto.from_dict(tenant_territory_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


