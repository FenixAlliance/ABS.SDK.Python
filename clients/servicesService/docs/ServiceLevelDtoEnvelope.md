# ServiceLevelDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ServiceLevelDto**](ServiceLevelDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_level_dto_envelope import ServiceLevelDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLevelDtoEnvelope from a JSON string
service_level_dto_envelope_instance = ServiceLevelDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ServiceLevelDtoEnvelope.to_json())

# convert the object into a dict
service_level_dto_envelope_dict = service_level_dto_envelope_instance.to_dict()
# create an instance of ServiceLevelDtoEnvelope from a dict
service_level_dto_envelope_from_dict = ServiceLevelDtoEnvelope.from_dict(service_level_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


