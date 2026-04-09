# CourseCohortDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**start_date_time** | **datetime** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 
**expected_start_date_time** | **datetime** |  | [optional] 
**expected_end_date_time** | **datetime** |  | [optional] 
**course_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_cohort_dto import CourseCohortDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCohortDto from a JSON string
course_cohort_dto_instance = CourseCohortDto.from_json(json)
# print the JSON string representation of the object
print(CourseCohortDto.to_json())

# convert the object into a dict
course_cohort_dto_dict = course_cohort_dto_instance.to_dict()
# create an instance of CourseCohortDto from a dict
course_cohort_dto_from_dict = CourseCohortDto.from_dict(course_cohort_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


