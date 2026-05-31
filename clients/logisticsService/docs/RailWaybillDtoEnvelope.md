# RailWaybillDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**RailWaybillDto**](RailWaybillDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.rail_waybill_dto_envelope import RailWaybillDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of RailWaybillDtoEnvelope from a JSON string
rail_waybill_dto_envelope_instance = RailWaybillDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(RailWaybillDtoEnvelope.to_json())

# convert the object into a dict
rail_waybill_dto_envelope_dict = rail_waybill_dto_envelope_instance.to_dict()
# create an instance of RailWaybillDtoEnvelope from a dict
rail_waybill_dto_envelope_from_dict = RailWaybillDtoEnvelope.from_dict(rail_waybill_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


