# CourseProblemSetDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**overall_score** | **float** |  | [optional] 
**course_id** | **str** |  | [optional] 
**course_unit_id** | **str** |  | [optional] 
**release_date_time** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.course_problem_set_dto import CourseProblemSetDto

# TODO update the JSON string below
json = "{}"
# create an instance of CourseProblemSetDto from a JSON string
course_problem_set_dto_instance = CourseProblemSetDto.from_json(json)
# print the JSON string representation of the object
print(CourseProblemSetDto.to_json())

# convert the object into a dict
course_problem_set_dto_dict = course_problem_set_dto_instance.to_dict()
# create an instance of CourseProblemSetDto from a dict
course_problem_set_dto_from_dict = CourseProblemSetDto.from_dict(course_problem_set_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


