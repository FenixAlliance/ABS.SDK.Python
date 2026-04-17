# CourseCohortCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**course_id** | **str** |  | 
**start_date_time** | **datetime** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 
**expected_start_date_time** | **datetime** |  | [optional] 
**expected_end_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_cohort_create_dto import CourseCohortCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCohortCreateDto from a JSON string
course_cohort_create_dto_instance = CourseCohortCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseCohortCreateDto.to_json())

# convert the object into a dict
course_cohort_create_dto_dict = course_cohort_create_dto_instance.to_dict()
# create an instance of CourseCohortCreateDto from a dict
course_cohort_create_dto_from_dict = CourseCohortCreateDto.from_dict(course_cohort_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


