# TruckDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TruckDto]**](TruckDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.truck_dto_list_envelope import TruckDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TruckDtoListEnvelope from a JSON string
truck_dto_list_envelope_instance = TruckDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TruckDtoListEnvelope.to_json())

# convert the object into a dict
truck_dto_list_envelope_dict = truck_dto_list_envelope_instance.to_dict()
# create an instance of TruckDtoListEnvelope from a dict
truck_dto_list_envelope_from_dict = TruckDtoListEnvelope.from_dict(truck_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


