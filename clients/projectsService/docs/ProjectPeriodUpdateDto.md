# ProjectPeriodUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start_date** | **datetime** |  | [optional] 
**period_end_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.project_period_update_dto import ProjectPeriodUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPeriodUpdateDto from a JSON string
project_period_update_dto_instance = ProjectPeriodUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectPeriodUpdateDto.to_json())

# convert the object into a dict
project_period_update_dto_dict = project_period_update_dto_instance.to_dict()
# create an instance of ProjectPeriodUpdateDto from a dict
project_period_update_dto_from_dict = ProjectPeriodUpdateDto.from_dict(project_period_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


