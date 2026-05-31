# ScheduleCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**sunday** | **bool** |  | [optional] 
**monday** | **bool** |  | [optional] 
**tuesday** | **bool** |  | [optional] 
**wednesday** | **bool** |  | [optional] 
**thursday** | **bool** |  | [optional] 
**friday** | **bool** |  | [optional] 
**saturday** | **bool** |  | [optional] 
**unique_interval** | **bool** |  | [optional] 
**is24x7_interval** | **bool** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 
**holiday_schedule_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_create_dto import ScheduleCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleCreateDto from a JSON string
schedule_create_dto_instance = ScheduleCreateDto.from_json(json)
# print the JSON string representation of the object
print(ScheduleCreateDto.to_json())

# convert the object into a dict
schedule_create_dto_dict = schedule_create_dto_instance.to_dict()
# create an instance of ScheduleCreateDto from a dict
schedule_create_dto_from_dict = ScheduleCreateDto.from_dict(schedule_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


