# CourseCompletionCertificateUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**student_profile_id** | **str** |  | [optional] 
**course_enrollment_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**course_completion_certificate_template_id** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_completion_certificate_update_dto import CourseCompletionCertificateUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletionCertificateUpdateDto from a JSON string
course_completion_certificate_update_dto_instance = CourseCompletionCertificateUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCompletionCertificateUpdateDto.to_json())

# convert the object into a dict
course_completion_certificate_update_dto_dict = course_completion_certificate_update_dto_instance.to_dict()
# create an instance of CourseCompletionCertificateUpdateDto from a dict
course_completion_certificate_update_dto_from_dict = CourseCompletionCertificateUpdateDto.from_dict(course_completion_certificate_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


