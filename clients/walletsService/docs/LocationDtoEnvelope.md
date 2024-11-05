# LocationDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**LocationDto**](LocationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_dto_envelope import LocationDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LocationDtoEnvelope from a JSON string
location_dto_envelope_instance = LocationDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(LocationDtoEnvelope.to_json())

# convert the object into a dict
location_dto_envelope_dict = location_dto_envelope_instance.to_dict()
# create an instance of LocationDtoEnvelope from a dict
location_dto_envelope_from_dict = LocationDtoEnvelope.from_dict(location_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


