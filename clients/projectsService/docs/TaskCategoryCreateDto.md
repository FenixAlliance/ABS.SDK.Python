# TaskCategoryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.task_category_create_dto import TaskCategoryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCategoryCreateDto from a JSON string
task_category_create_dto_instance = TaskCategoryCreateDto.from_json(json)
# print the JSON string representation of the object
print(TaskCategoryCreateDto.to_json())

# convert the object into a dict
task_category_create_dto_dict = task_category_create_dto_instance.to_dict()
# create an instance of TaskCategoryCreateDto from a dict
task_category_create_dto_from_dict = TaskCategoryCreateDto.from_dict(task_category_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


