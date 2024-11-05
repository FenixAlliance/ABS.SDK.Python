# ProjectTimeLogUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_date** | **datetime** |  | [optional] 
**time_span** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**project_task_id** | **str** |  | [optional] 
**project_period_id** | **str** |  | [optional] 
**project_time_log_record_type** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.project_time_log_update_dto import ProjectTimeLogUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTimeLogUpdateDto from a JSON string
project_time_log_update_dto_instance = ProjectTimeLogUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectTimeLogUpdateDto.to_json())

# convert the object into a dict
project_time_log_update_dto_dict = project_time_log_update_dto_instance.to_dict()
# create an instance of ProjectTimeLogUpdateDto from a dict
project_time_log_update_dto_from_dict = ProjectTimeLogUpdateDto.from_dict(project_time_log_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


