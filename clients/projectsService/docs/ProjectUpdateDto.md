# ProjectUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**project_start_date** | **datetime** |  | [optional] 
**project_end_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.project_update_dto import ProjectUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdateDto from a JSON string
project_update_dto_instance = ProjectUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ProjectUpdateDto.to_json())

# convert the object into a dict
project_update_dto_dict = project_update_dto_instance.to_dict()
# create an instance of ProjectUpdateDto from a dict
project_update_dto_from_dict = ProjectUpdateDto.from_dict(project_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


