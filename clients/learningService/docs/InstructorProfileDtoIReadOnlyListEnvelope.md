# InstructorProfileDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[InstructorProfileDto]**](InstructorProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.instructor_profile_dto_i_read_only_list_envelope import InstructorProfileDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InstructorProfileDtoIReadOnlyListEnvelope from a JSON string
instructor_profile_dto_i_read_only_list_envelope_instance = InstructorProfileDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(InstructorProfileDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
instructor_profile_dto_i_read_only_list_envelope_dict = instructor_profile_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of InstructorProfileDtoIReadOnlyListEnvelope from a dict
instructor_profile_dto_i_read_only_list_envelope_from_dict = InstructorProfileDtoIReadOnlyListEnvelope.from_dict(instructor_profile_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


