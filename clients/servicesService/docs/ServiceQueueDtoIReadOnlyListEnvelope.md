# ServiceQueueDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ServiceQueueDto]**](ServiceQueueDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_queue_dto_i_read_only_list_envelope import ServiceQueueDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQueueDtoIReadOnlyListEnvelope from a JSON string
service_queue_dto_i_read_only_list_envelope_instance = ServiceQueueDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ServiceQueueDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
service_queue_dto_i_read_only_list_envelope_dict = service_queue_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of ServiceQueueDtoIReadOnlyListEnvelope from a dict
service_queue_dto_i_read_only_list_envelope_from_dict = ServiceQueueDtoIReadOnlyListEnvelope.from_dict(service_queue_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


