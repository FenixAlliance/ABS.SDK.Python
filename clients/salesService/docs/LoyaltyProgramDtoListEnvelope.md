# LoyaltyProgramDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LoyaltyProgramDto]**](LoyaltyProgramDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.loyalty_program_dto_list_envelope import LoyaltyProgramDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyProgramDtoListEnvelope from a JSON string
loyalty_program_dto_list_envelope_instance = LoyaltyProgramDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LoyaltyProgramDtoListEnvelope.to_json())

# convert the object into a dict
loyalty_program_dto_list_envelope_dict = loyalty_program_dto_list_envelope_instance.to_dict()
# create an instance of LoyaltyProgramDtoListEnvelope from a dict
loyalty_program_dto_list_envelope_from_dict = LoyaltyProgramDtoListEnvelope.from_dict(loyalty_program_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


