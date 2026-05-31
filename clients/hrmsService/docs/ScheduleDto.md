# ScheduleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
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
from openapi_client.models.schedule_dto import ScheduleDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDto from a JSON string
schedule_dto_instance = ScheduleDto.from_json(json)
# print the JSON string representation of the object
print(ScheduleDto.to_json())

# convert the object into a dict
schedule_dto_dict = schedule_dto_instance.to_dict()
# create an instance of ScheduleDto from a dict
schedule_dto_from_dict = ScheduleDto.from_dict(schedule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


