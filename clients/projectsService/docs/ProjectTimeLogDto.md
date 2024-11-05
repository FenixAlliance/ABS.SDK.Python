# ProjectTimeLogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**project_id** | **str** |  | [optional] 
**project_task_id** | **str** |  | [optional] 
**task_category_id** | **str** |  | [optional] 
**project_period_id** | **str** |  | [optional] 
**responsible_contact_id** | **str** |  | [optional] 
**creator_contact_id** | **str** |  | [optional] 
**record_type** | **int** |  | [optional] 
**time_stamp** | **datetime** |  | [optional] 
**time_span** | **str** |  | [optional] 
**log_date** | **datetime** |  | [optional] 
**comments** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_time_log_dto import ProjectTimeLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTimeLogDto from a JSON string
project_time_log_dto_instance = ProjectTimeLogDto.from_json(json)
# print the JSON string representation of the object
print(ProjectTimeLogDto.to_json())

# convert the object into a dict
project_time_log_dto_dict = project_time_log_dto_instance.to_dict()
# create an instance of ProjectTimeLogDto from a dict
project_time_log_dto_from_dict = ProjectTimeLogDto.from_dict(project_time_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


