# TruckTripDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**trip_number** | **str** |  | [optional] 
**truck_trip_status** | **str** |  | [optional] 
**container_number** | **str** |  | [optional] 
**seal_number** | **str** |  | [optional] 
**departure_time** | **datetime** |  | [optional] 
**arrival_time** | **datetime** |  | [optional] 
**actual_departure_time** | **datetime** |  | [optional] 
**actual_arrival_time** | **datetime** |  | [optional] 
**distance_km** | **float** |  | [optional] 
**notes** | **str** |  | [optional] 
**truck_id** | **str** |  | [optional] 
**origin_port_id** | **str** |  | [optional] 
**origin_location_id** | **str** |  | [optional] 
**destination_port_id** | **str** |  | [optional] 
**destination_location_id** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**bill_of_lading_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.truck_trip_dto import TruckTripDto

# TODO update the JSON string below
json = "{}"
# create an instance of TruckTripDto from a JSON string
truck_trip_dto_instance = TruckTripDto.from_json(json)
# print the JSON string representation of the object
print(TruckTripDto.to_json())

# convert the object into a dict
truck_trip_dto_dict = truck_trip_dto_instance.to_dict()
# create an instance of TruckTripDto from a dict
truck_trip_dto_from_dict = TruckTripDto.from_dict(truck_trip_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


