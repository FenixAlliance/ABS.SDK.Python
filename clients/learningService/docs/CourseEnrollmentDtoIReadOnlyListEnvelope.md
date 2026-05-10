# CourseEnrollmentDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CourseEnrollmentDto]**](CourseEnrollmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.course_enrollment_dto_i_read_only_list_envelope import CourseEnrollmentDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CourseEnrollmentDtoIReadOnlyListEnvelope from a JSON string
course_enrollment_dto_i_read_only_list_envelope_instance = CourseEnrollmentDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CourseEnrollmentDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
course_enrollment_dto_i_read_only_list_envelope_dict = course_enrollment_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of CourseEnrollmentDtoIReadOnlyListEnvelope from a dict
course_enrollment_dto_i_read_only_list_envelope_from_dict = CourseEnrollmentDtoIReadOnlyListEnvelope.from_dict(course_enrollment_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


