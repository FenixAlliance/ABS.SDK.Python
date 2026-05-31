# PortDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PortDto**](PortDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.port_dto_envelope import PortDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PortDtoEnvelope from a JSON string
port_dto_envelope_instance = PortDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PortDtoEnvelope.to_json())

# convert the object into a dict
port_dto_envelope_dict = port_dto_envelope_instance.to_dict()
# create an instance of PortDtoEnvelope from a dict
port_dto_envelope_from_dict = PortDtoEnvelope.from_dict(port_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


