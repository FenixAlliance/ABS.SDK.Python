# TruckTripDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TruckTripDto]**](TruckTripDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.truck_trip_dto_list_envelope import TruckTripDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TruckTripDtoListEnvelope from a JSON string
truck_trip_dto_list_envelope_instance = TruckTripDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TruckTripDtoListEnvelope.to_json())

# convert the object into a dict
truck_trip_dto_list_envelope_dict = truck_trip_dto_list_envelope_instance.to_dict()
# create an instance of TruckTripDtoListEnvelope from a dict
truck_trip_dto_list_envelope_from_dict = TruckTripDtoListEnvelope.from_dict(truck_trip_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


