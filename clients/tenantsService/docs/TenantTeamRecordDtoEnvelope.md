# TenantTeamRecordDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TenantTeamRecordDto**](TenantTeamRecordDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tenant_team_record_dto_envelope import TenantTeamRecordDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTeamRecordDtoEnvelope from a JSON string
tenant_team_record_dto_envelope_instance = TenantTeamRecordDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TenantTeamRecordDtoEnvelope.to_json())

# convert the object into a dict
tenant_team_record_dto_envelope_dict = tenant_team_record_dto_envelope_instance.to_dict()
# create an instance of TenantTeamRecordDtoEnvelope from a dict
tenant_team_record_dto_envelope_from_dict = TenantTeamRecordDtoEnvelope.from_dict(tenant_team_record_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


