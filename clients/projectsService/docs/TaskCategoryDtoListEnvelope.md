# TaskCategoryDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TaskCategoryDto]**](TaskCategoryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.task_category_dto_list_envelope import TaskCategoryDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCategoryDtoListEnvelope from a JSON string
task_category_dto_list_envelope_instance = TaskCategoryDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TaskCategoryDtoListEnvelope.to_json())

# convert the object into a dict
task_category_dto_list_envelope_dict = task_category_dto_list_envelope_instance.to_dict()
# create an instance of TaskCategoryDtoListEnvelope from a dict
task_category_dto_list_envelope_from_dict = TaskCategoryDtoListEnvelope.from_dict(task_category_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

