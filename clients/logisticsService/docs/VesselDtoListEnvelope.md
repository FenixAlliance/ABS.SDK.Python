# VesselDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[VesselDto]**](VesselDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.vessel_dto_list_envelope import VesselDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of VesselDtoListEnvelope from a JSON string
vessel_dto_list_envelope_instance = VesselDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(VesselDtoListEnvelope.to_json())

# convert the object into a dict
vessel_dto_list_envelope_dict = vessel_dto_list_envelope_instance.to_dict()
# create an instance of VesselDtoListEnvelope from a dict
vessel_dto_list_envelope_from_dict = VesselDtoListEnvelope.from_dict(vessel_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


