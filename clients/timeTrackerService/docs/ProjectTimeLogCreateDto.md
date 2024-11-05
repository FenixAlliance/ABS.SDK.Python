# ProjectTimeLogCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**time_span** | **str** |  | [optional] 
**log_date** | **datetime** |  | [optional] 
**comments** | **str** |  | [optional] 
**project_task_id** | **str** |  | 
**project_period_id** | **str** |  | 
**project_time_log_record_type** | **int** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_time_log_create_dto import ProjectTimeLogCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTimeLogCreateDto from a JSON string
project_time_log_create_dto_instance = ProjectTimeLogCreateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectTimeLogCreateDto.to_json())

# convert the object into a dict
project_time_log_create_dto_dict = project_time_log_create_dto_instance.to_dict()
# create an instance of ProjectTimeLogCreateDto from a dict
project_time_log_create_dto_from_dict = ProjectTimeLogCreateDto.from_dict(project_time_log_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


