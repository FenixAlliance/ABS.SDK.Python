# CourseCompletionCertificateCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**student_profile_id** | **str** |  | 
**course_enrollment_id** | **str** |  | 
**course_completion_certificate_template_id** | **str** |  | [optional] 
**course_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_completion_certificate_create_dto import CourseCompletionCertificateCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletionCertificateCreateDto from a JSON string
course_completion_certificate_create_dto_instance = CourseCompletionCertificateCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCompletionCertificateCreateDto.to_json())

# convert the object into a dict
course_completion_certificate_create_dto_dict = course_completion_certificate_create_dto_instance.to_dict()
# create an instance of CourseCompletionCertificateCreateDto from a dict
course_completion_certificate_create_dto_from_dict = CourseCompletionCertificateCreateDto.from_dict(course_completion_certificate_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


