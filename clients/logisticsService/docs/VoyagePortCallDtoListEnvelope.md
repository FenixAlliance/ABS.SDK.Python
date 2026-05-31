# VoyagePortCallDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[VoyagePortCallDto]**](VoyagePortCallDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.voyage_port_call_dto_list_envelope import VoyagePortCallDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of VoyagePortCallDtoListEnvelope from a JSON string
voyage_port_call_dto_list_envelope_instance = VoyagePortCallDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(VoyagePortCallDtoListEnvelope.to_json())

# convert the object into a dict
voyage_port_call_dto_list_envelope_dict = voyage_port_call_dto_list_envelope_instance.to_dict()
# create an instance of VoyagePortCallDtoListEnvelope from a dict
voyage_port_call_dto_list_envelope_from_dict = VoyagePortCallDtoListEnvelope.from_dict(voyage_port_call_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


