# ShiftDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
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
**tenant_id** | **str** |  | [optional] 
**employee_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shift_dto import ShiftDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftDto from a JSON string
shift_dto_instance = ShiftDto.from_json(json)
# print the JSON string representation of the object
print(ShiftDto.to_json())

# convert the object into a dict
shift_dto_dict = shift_dto_instance.to_dict()
# create an instance of ShiftDto from a dict
shift_dto_from_dict = ShiftDto.from_dict(shift_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


