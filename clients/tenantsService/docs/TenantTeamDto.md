# TenantTeamDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**business_unit_id** | **str** |  | [optional] 
**organization_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_dto import TenantTeamDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamDto from a JSON string
tenant_team_dto_instance = TenantTeamDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamDto.to_json())

# convert the object into a dict
tenant_team_dto_dict = tenant_team_dto_instance.to_dict()
# create an instance of TenantTeamDto from a dict
tenant_team_dto_from_dict = TenantTeamDto.from_dict(tenant_team_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


