# LogDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[LogDto]**](LogDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.log_dto_list_envelope import LogDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of LogDtoListEnvelope from a JSON string
log_dto_list_envelope_instance = LogDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(LogDtoListEnvelope.to_json())

# convert the object into a dict
log_dto_list_envelope_dict = log_dto_list_envelope_instance.to_dict()
# create an instance of LogDtoListEnvelope from a dict
log_dto_list_envelope_from_dict = LogDtoListEnvelope.from_dict(log_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


