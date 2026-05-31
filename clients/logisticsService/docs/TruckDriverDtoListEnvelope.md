# TruckDriverDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TruckDriverDto]**](TruckDriverDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.truck_driver_dto_list_envelope import TruckDriverDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TruckDriverDtoListEnvelope from a JSON string
truck_driver_dto_list_envelope_instance = TruckDriverDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TruckDriverDtoListEnvelope.to_json())

# convert the object into a dict
truck_driver_dto_list_envelope_dict = truck_driver_dto_list_envelope_instance.to_dict()
# create an instance of TruckDriverDtoListEnvelope from a dict
truck_driver_dto_list_envelope_from_dict = TruckDriverDtoListEnvelope.from_dict(truck_driver_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


