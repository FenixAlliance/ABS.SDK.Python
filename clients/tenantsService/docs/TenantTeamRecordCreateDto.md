# TenantTeamRecordCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_team_id** | **str** |  | 

## Example

```python
from openapi_client.models.tenant_team_record_create_dto import TenantTeamRecordCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamRecordCreateDto from a JSON string
tenant_team_record_create_dto_instance = TenantTeamRecordCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamRecordCreateDto.to_json())

# convert the object into a dict
tenant_team_record_create_dto_dict = tenant_team_record_create_dto_instance.to_dict()
# create an instance of TenantTeamRecordCreateDto from a dict
tenant_team_record_create_dto_from_dict = TenantTeamRecordCreateDto.from_dict(tenant_team_record_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


