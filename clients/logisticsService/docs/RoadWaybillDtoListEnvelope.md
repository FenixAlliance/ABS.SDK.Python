# RoadWaybillDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[RoadWaybillDto]**](RoadWaybillDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.road_waybill_dto_list_envelope import RoadWaybillDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of RoadWaybillDtoListEnvelope from a JSON string
road_waybill_dto_list_envelope_instance = RoadWaybillDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(RoadWaybillDtoListEnvelope.to_json())

# convert the object into a dict
road_waybill_dto_list_envelope_dict = road_waybill_dto_list_envelope_instance.to_dict()
# create an instance of RoadWaybillDtoListEnvelope from a dict
road_waybill_dto_list_envelope_from_dict = RoadWaybillDtoListEnvelope.from_dict(road_waybill_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


