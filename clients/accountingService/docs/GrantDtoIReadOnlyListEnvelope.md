# GrantDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[GrantDto]**](GrantDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.grant_dto_i_read_only_list_envelope import GrantDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of GrantDtoIReadOnlyListEnvelope from a JSON string
grant_dto_i_read_only_list_envelope_instance = GrantDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(GrantDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
grant_dto_i_read_only_list_envelope_dict = grant_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of GrantDtoIReadOnlyListEnvelope from a dict
grant_dto_i_read_only_list_envelope_from_dict = GrantDtoIReadOnlyListEnvelope.from_dict(grant_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


