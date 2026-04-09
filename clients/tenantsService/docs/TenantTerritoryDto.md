# TenantTerritoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**parent_territory_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_territory_dto import TenantTerritoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTerritoryDto from a JSON string
tenant_territory_dto_instance = TenantTerritoryDto.from_json(json)
# print the JSON string representation of the object
print(TenantTerritoryDto.to_json())

# convert the object into a dict
tenant_territory_dto_dict = tenant_territory_dto_instance.to_dict()
# create an instance of TenantTerritoryDto from a dict
tenant_territory_dto_from_dict = TenantTerritoryDto.from_dict(tenant_territory_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


