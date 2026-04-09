# CourseCompletionCertificateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**student_profile_id** | **str** |  | [optional] 
**course_enrollment_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**course_completion_certificate_template_id** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 
**student_name** | **str** |  | [optional] 
**student_last_name** | **str** |  | [optional] 
**course_title** | **str** |  | [optional] 
**total_effort_in_hours** | **float** |  | [optional] 
**instructor_name** | **str** |  | [optional] 
**instructor_last_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_completion_certificate_dto import CourseCompletionCertificateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletionCertificateDto from a JSON string
course_completion_certificate_dto_instance = CourseCompletionCertificateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCompletionCertificateDto.to_json())

# convert the object into a dict
course_completion_certificate_dto_dict = course_completion_certificate_dto_instance.to_dict()
# create an instance of CourseCompletionCertificateDto from a dict
course_completion_certificate_dto_from_dict = CourseCompletionCertificateDto.from_dict(course_completion_certificate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


