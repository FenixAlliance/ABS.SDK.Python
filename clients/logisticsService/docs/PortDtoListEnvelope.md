# PortDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PortDto]**](PortDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.port_dto_list_envelope import PortDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PortDtoListEnvelope from a JSON string
port_dto_list_envelope_instance = PortDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PortDtoListEnvelope.to_json())

# convert the object into a dict
port_dto_list_envelope_dict = port_dto_list_envelope_instance.to_dict()
# create an instance of PortDtoListEnvelope from a dict
port_dto_list_envelope_from_dict = PortDtoListEnvelope.from_dict(port_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


