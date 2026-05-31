# RoundingPolicyDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[RoundingPolicyDto]**](RoundingPolicyDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.rounding_policy_dto_list_envelope import RoundingPolicyDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingPolicyDtoListEnvelope from a JSON string
rounding_policy_dto_list_envelope_instance = RoundingPolicyDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(RoundingPolicyDtoListEnvelope.to_json())

# convert the object into a dict
rounding_policy_dto_list_envelope_dict = rounding_policy_dto_list_envelope_instance.to_dict()
# create an instance of RoundingPolicyDtoListEnvelope from a dict
rounding_policy_dto_list_envelope_from_dict = RoundingPolicyDtoListEnvelope.from_dict(rounding_policy_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


