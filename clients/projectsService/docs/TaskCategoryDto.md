# TaskCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.task_category_dto import TaskCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCategoryDto from a JSON string
task_category_dto_instance = TaskCategoryDto.from_json(json)
# print the JSON string representation of the object
print(TaskCategoryDto.to_json())

# convert the object into a dict
task_category_dto_dict = task_category_dto_instance.to_dict()
# create an instance of TaskCategoryDto from a dict
task_category_dto_from_dict = TaskCategoryDto.from_dict(task_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


