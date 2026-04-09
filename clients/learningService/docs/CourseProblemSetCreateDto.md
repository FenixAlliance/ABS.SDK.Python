# CourseProblemSetCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**overall_score** | **float** |  | [optional] 
**course_id** | **str** |  | 
**business_id** | **str** |  | 
**course_unit_id** | **str** |  | [optional] 
**course_grading_rubric_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.course_problem_set_create_dto import CourseProblemSetCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseProblemSetCreateDto from a JSON string
course_problem_set_create_dto_instance = CourseProblemSetCreateDto.from_json(json)
# print the JSON string representation of the object
print(CourseProblemSetCreateDto.to_json())

# convert the object into a dict
course_problem_set_create_dto_dict = course_problem_set_create_dto_instance.to_dict()
# create an instance of CourseProblemSetCreateDto from a dict
course_problem_set_create_dto_from_dict = CourseProblemSetCreateDto.from_dict(course_problem_set_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


