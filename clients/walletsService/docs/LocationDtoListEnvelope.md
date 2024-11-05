# LocationDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LocationDto]**](LocationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_dto_list_envelope import LocationDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LocationDtoListEnvelope from a JSON string
location_dto_list_envelope_instance = LocationDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LocationDtoListEnvelope.to_json())

# convert the object into a dict
location_dto_list_envelope_dict = location_dto_list_envelope_instance.to_dict()
# create an instance of LocationDtoListEnvelope from a dict
location_dto_list_envelope_from_dict = LocationDtoListEnvelope.from_dict(location_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


