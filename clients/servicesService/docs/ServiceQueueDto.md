# ServiceQueueDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_queue_dto import ServiceQueueDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQueueDto from a JSON string
service_queue_dto_instance = ServiceQueueDto.from_json(json)
# print the JSON string representation of the object
print(ServiceQueueDto.to_json())

# convert the object into a dict
service_queue_dto_dict = service_queue_dto_instance.to_dict()
# create an instance of ServiceQueueDto from a dict
service_queue_dto_from_dict = ServiceQueueDto.from_dict(service_queue_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


