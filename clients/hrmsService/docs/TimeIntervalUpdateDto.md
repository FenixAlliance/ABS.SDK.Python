# TimeIntervalUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_break** | **bool** |  | [optional] 
**occust_on_monday** | **bool** |  | [optional] 
**occust_on_tuesday** | **bool** |  | [optional] 
**occust_on_wednesday** | **bool** |  | [optional] 
**occust_on_thursday** | **bool** |  | [optional] 
**occust_on_friday** | **bool** |  | [optional] 
**occust_on_saturday** | **bool** |  | [optional] 
**occust_on_sunday** | **bool** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**repeat_every** | **int** |  | [optional] 
**parent_time_interval_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.time_interval_update_dto import TimeIntervalUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimeIntervalUpdateDto from a JSON string
time_interval_update_dto_instance = TimeIntervalUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TimeIntervalUpdateDto.to_json())

# convert the object into a dict
time_interval_update_dto_dict = time_interval_update_dto_instance.to_dict()
# create an instance of TimeIntervalUpdateDto from a dict
time_interval_update_dto_from_dict = TimeIntervalUpdateDto.from_dict(time_interval_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


