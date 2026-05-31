# TrainingProgramEventUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**is_break** | **bool** |  | [optional] 
**occust_on_monday** | **bool** |  | [optional] 
**occust_on_tuesday** | **bool** |  | [optional] 
**occust_on_wednesday** | **bool** |  | [optional] 
**occust_on_thursday** | **bool** |  | [optional] 
**occust_on_friday** | **bool** |  | [optional] 
**occust_on_saturday** | **bool** |  | [optional] 
**occust_on_sunday** | **bool** |  | [optional] 
**repeat_every** | **int** |  | [optional] 
**repetition_criteria** | **str** |  | [optional] 
**recurrence_start** | **datetime** |  | [optional] 
**recurrence_end** | **datetime** |  | [optional] 
**day_of_the_week** | **str** |  | [optional] 
**schedule_id** | **str** |  | [optional] 
**parent_time_interval_id** | **str** |  | [optional] 
**training_program_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.training_program_event_update_dto import TrainingProgramEventUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrainingProgramEventUpdateDto from a JSON string
training_program_event_update_dto_instance = TrainingProgramEventUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TrainingProgramEventUpdateDto.to_json())

# convert the object into a dict
training_program_event_update_dto_dict = training_program_event_update_dto_instance.to_dict()
# create an instance of TrainingProgramEventUpdateDto from a dict
training_program_event_update_dto_from_dict = TrainingProgramEventUpdateDto.from_dict(training_program_event_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


