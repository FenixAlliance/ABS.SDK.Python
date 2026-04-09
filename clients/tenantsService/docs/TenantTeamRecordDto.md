# TenantTeamRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**team_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_record_dto import TenantTeamRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamRecordDto from a JSON string
tenant_team_record_dto_instance = TenantTeamRecordDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamRecordDto.to_json())

# convert the object into a dict
tenant_team_record_dto_dict = tenant_team_record_dto_instance.to_dict()
# create an instance of TenantTeamRecordDto from a dict
tenant_team_record_dto_from_dict = TenantTeamRecordDto.from_dict(tenant_team_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


