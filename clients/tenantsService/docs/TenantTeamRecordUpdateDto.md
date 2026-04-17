# TenantTeamRecordUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_team_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_record_update_dto import TenantTeamRecordUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamRecordUpdateDto from a JSON string
tenant_team_record_update_dto_instance = TenantTeamRecordUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantTeamRecordUpdateDto.to_json())

# convert the object into a dict
tenant_team_record_update_dto_dict = tenant_team_record_update_dto_instance.to_dict()
# create an instance of TenantTeamRecordUpdateDto from a dict
tenant_team_record_update_dto_from_dict = TenantTeamRecordUpdateDto.from_dict(tenant_team_record_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


