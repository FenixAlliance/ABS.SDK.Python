# TenantTeamCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**business_unit_id** | **str** |  | [optional] 
**organization_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_create_dto import TenantTeamCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamCreateDto from a JSON string
tenant_team_create_dto_instance = TenantTeamCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamCreateDto.to_json())

# convert the object into a dict
tenant_team_create_dto_dict = tenant_team_create_dto_instance.to_dict()
# create an instance of TenantTeamCreateDto from a dict
tenant_team_create_dto_from_dict = TenantTeamCreateDto.from_dict(tenant_team_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


