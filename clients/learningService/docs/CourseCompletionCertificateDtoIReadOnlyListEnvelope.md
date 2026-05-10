# CourseCompletionCertificateDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CourseCompletionCertificateDto]**](CourseCompletionCertificateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.course_completion_certificate_dto_i_read_only_list_envelope import CourseCompletionCertificateDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletionCertificateDtoIReadOnlyListEnvelope from a JSON string
course_completion_certificate_dto_i_read_only_list_envelope_instance = CourseCompletionCertificateDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CourseCompletionCertificateDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
course_completion_certificate_dto_i_read_only_list_envelope_dict = course_completion_certificate_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of CourseCompletionCertificateDtoIReadOnlyListEnvelope from a dict
course_completion_certificate_dto_i_read_only_list_envelope_from_dict = CourseCompletionCertificateDtoIReadOnlyListEnvelope.from_dict(course_completion_certificate_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


