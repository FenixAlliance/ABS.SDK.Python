# CourseEnrollmentUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**course_cohort_id** | **str** |  | [optional] 
**course_completion_certificate_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_enrollment_update_dto import CourseEnrollmentUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseEnrollmentUpdateDto from a JSON string
course_enrollment_update_dto_instance = CourseEnrollmentUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseEnrollmentUpdateDto.to_json())

# convert the object into a dict
course_enrollment_update_dto_dict = course_enrollment_update_dto_instance.to_dict()
# create an instance of CourseEnrollmentUpdateDto from a dict
course_enrollment_update_dto_from_dict = CourseEnrollmentUpdateDto.from_dict(course_enrollment_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


