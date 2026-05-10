# ReturnRequestDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ReturnRequestDto]**](ReturnRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_request_dto_list_envelope import ReturnRequestDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRequestDtoListEnvelope from a JSON string
return_request_dto_list_envelope_instance = ReturnRequestDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ReturnRequestDtoListEnvelope.to_json())

# convert the object into a dict
return_request_dto_list_envelope_dict = return_request_dto_list_envelope_instance.to_dict()
# create an instance of ReturnRequestDtoListEnvelope from a dict
return_request_dto_list_envelope_from_dict = ReturnRequestDtoListEnvelope.from_dict(return_request_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


