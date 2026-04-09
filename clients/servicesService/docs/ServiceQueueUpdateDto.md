# ServiceQueueUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_queue_update_dto import ServiceQueueUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQueueUpdateDto from a JSON string
service_queue_update_dto_instance = ServiceQueueUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ServiceQueueUpdateDto.to_json())

# convert the object into a dict
service_queue_update_dto_dict = service_queue_update_dto_instance.to_dict()
# create an instance of ServiceQueueUpdateDto from a dict
service_queue_update_dto_from_dict = ServiceQueueUpdateDto.from_dict(service_queue_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


