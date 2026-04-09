# ServiceDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ServiceDto]**](ServiceDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_dto_i_read_only_list_envelope import ServiceDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDtoIReadOnlyListEnvelope from a JSON string
service_dto_i_read_only_list_envelope_instance = ServiceDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ServiceDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
service_dto_i_read_only_list_envelope_dict = service_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of ServiceDtoIReadOnlyListEnvelope from a dict
service_dto_i_read_only_list_envelope_from_dict = ServiceDtoIReadOnlyListEnvelope.from_dict(service_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


