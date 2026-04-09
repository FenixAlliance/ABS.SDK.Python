# CourseCohortUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**start_date_time** | **datetime** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 
**expected_start_date_time** | **datetime** |  | [optional] 
**expected_end_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_cohort_update_dto import CourseCohortUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCohortUpdateDto from a JSON string
course_cohort_update_dto_instance = CourseCohortUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCohortUpdateDto.to_json())

# convert the object into a dict
course_cohort_update_dto_dict = course_cohort_update_dto_instance.to_dict()
# create an instance of CourseCohortUpdateDto from a dict
course_cohort_update_dto_from_dict = CourseCohortUpdateDto.from_dict(course_cohort_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


