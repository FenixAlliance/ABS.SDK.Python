# GrantDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**GrantDto**](GrantDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.grant_dto_envelope import GrantDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GrantDtoEnvelope from a JSON string
grant_dto_envelope_instance = GrantDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(GrantDtoEnvelope.to_json())

# convert the object into a dict
grant_dto_envelope_dict = grant_dto_envelope_instance.to_dict()
# create an instance of GrantDtoEnvelope from a dict
grant_dto_envelope_from_dict = GrantDtoEnvelope.from_dict(grant_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


