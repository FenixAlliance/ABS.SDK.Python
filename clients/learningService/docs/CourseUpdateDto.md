# CourseUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**course_category_id** | **str** |  | [optional] 
**instructor_profile_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**regular_price** | **float** |  | [optional] 
**max_course_enrollments** | **int** |  | [optional] 
**total_effort_in_weeks** | **int** |  | [optional] 
**total_hours_per_week** | **int** |  | [optional] 
**total_effort_in_hours** | **int** |  | [optional] 
**start_date_time** | **datetime** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 
**inscriptions_start_date_time** | **datetime** |  | [optional] 
**inscriptions_end_date_time** | **datetime** |  | [optional] 
**published** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.course_update_dto import CourseUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseUpdateDto from a JSON string
course_update_dto_instance = CourseUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CourseUpdateDto.to_json())

# convert the object into a dict
course_update_dto_dict = course_update_dto_instance.to_dict()
# create an instance of CourseUpdateDto from a dict
course_update_dto_from_dict = CourseUpdateDto.from_dict(course_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


