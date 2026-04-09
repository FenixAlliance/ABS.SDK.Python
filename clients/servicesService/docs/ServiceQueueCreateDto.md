# ServiceQueueCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_queue_create_dto import ServiceQueueCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQueueCreateDto from a JSON string
service_queue_create_dto_instance = ServiceQueueCreateDto.from_json(json)
# print the JSON string representation of the object
print(ServiceQueueCreateDto.to_json())

# convert the object into a dict
service_queue_create_dto_dict = service_queue_create_dto_instance.to_dict()
# create an instance of ServiceQueueCreateDto from a dict
service_queue_create_dto_from_dict = ServiceQueueCreateDto.from_dict(service_queue_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


