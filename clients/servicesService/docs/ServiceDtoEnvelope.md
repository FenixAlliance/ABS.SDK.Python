# ServiceDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ServiceDto**](ServiceDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_dto_envelope import ServiceDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDtoEnvelope from a JSON string
service_dto_envelope_instance = ServiceDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ServiceDtoEnvelope.to_json())

# convert the object into a dict
service_dto_envelope_dict = service_dto_envelope_instance.to_dict()
# create an instance of ServiceDtoEnvelope from a dict
service_dto_envelope_from_dict = ServiceDtoEnvelope.from_dict(service_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


