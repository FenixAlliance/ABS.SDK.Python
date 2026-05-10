# StudentProfileDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[StudentProfileDto]**](StudentProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.student_profile_dto_i_read_only_list_envelope import StudentProfileDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of StudentProfileDtoIReadOnlyListEnvelope from a JSON string
student_profile_dto_i_read_only_list_envelope_instance = StudentProfileDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(StudentProfileDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
student_profile_dto_i_read_only_list_envelope_dict = student_profile_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of StudentProfileDtoIReadOnlyListEnvelope from a dict
student_profile_dto_i_read_only_list_envelope_from_dict = StudentProfileDtoIReadOnlyListEnvelope.from_dict(student_profile_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


