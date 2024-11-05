# ProjectPeriodCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**period_start_date** | **datetime** |  | [optional] 
**period_end_date** | **datetime** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.project_period_create_dto import ProjectPeriodCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPeriodCreateDto from a JSON string
project_period_create_dto_instance = ProjectPeriodCreateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectPeriodCreateDto.to_json())

# convert the object into a dict
project_period_create_dto_dict = project_period_create_dto_instance.to_dict()
# create an instance of ProjectPeriodCreateDto from a dict
project_period_create_dto_from_dict = ProjectPeriodCreateDto.from_dict(project_period_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


