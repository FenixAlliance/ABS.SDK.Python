# EmployerProfileDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**EmployerProfileDto**](EmployerProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.employer_profile_dto_envelope import EmployerProfileDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmployerProfileDtoEnvelope from a JSON string
employer_profile_dto_envelope_instance = EmployerProfileDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmployerProfileDtoEnvelope.to_json())

# convert the object into a dict
employer_profile_dto_envelope_dict = employer_profile_dto_envelope_instance.to_dict()
# create an instance of EmployerProfileDtoEnvelope from a dict
employer_profile_dto_envelope_from_dict = EmployerProfileDtoEnvelope.from_dict(employer_profile_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


