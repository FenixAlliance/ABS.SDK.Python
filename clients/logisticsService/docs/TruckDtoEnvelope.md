# TruckDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TruckDto**](TruckDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.truck_dto_envelope import TruckDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TruckDtoEnvelope from a JSON string
truck_dto_envelope_instance = TruckDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TruckDtoEnvelope.to_json())

# convert the object into a dict
truck_dto_envelope_dict = truck_dto_envelope_instance.to_dict()
# create an instance of TruckDtoEnvelope from a dict
truck_dto_envelope_from_dict = TruckDtoEnvelope.from_dict(truck_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


