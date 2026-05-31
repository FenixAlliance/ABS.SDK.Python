# TruckDriverDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TruckDriverDto**](TruckDriverDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.truck_driver_dto_envelope import TruckDriverDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TruckDriverDtoEnvelope from a JSON string
truck_driver_dto_envelope_instance = TruckDriverDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TruckDriverDtoEnvelope.to_json())

# convert the object into a dict
truck_driver_dto_envelope_dict = truck_driver_dto_envelope_instance.to_dict()
# create an instance of TruckDriverDtoEnvelope from a dict
truck_driver_dto_envelope_from_dict = TruckDriverDtoEnvelope.from_dict(truck_driver_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


