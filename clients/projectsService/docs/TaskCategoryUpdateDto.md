# TaskCategoryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.task_category_update_dto import TaskCategoryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCategoryUpdateDto from a JSON string
task_category_update_dto_instance = TaskCategoryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TaskCategoryUpdateDto.to_json())

# convert the object into a dict
task_category_update_dto_dict = task_category_update_dto_instance.to_dict()
# create an instance of TaskCategoryUpdateDto from a dict
task_category_update_dto_from_dict = TaskCategoryUpdateDto.from_dict(task_category_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

