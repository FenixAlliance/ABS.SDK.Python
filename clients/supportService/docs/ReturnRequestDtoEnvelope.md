# ReturnRequestDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ReturnRequestDto**](ReturnRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_request_dto_envelope import ReturnRequestDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnRequestDtoEnvelope from a JSON string
return_request_dto_envelope_instance = ReturnRequestDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ReturnRequestDtoEnvelope.to_json())

# convert the object into a dict
return_request_dto_envelope_dict = return_request_dto_envelope_instance.to_dict()
# create an instance of ReturnRequestDtoEnvelope from a dict
return_request_dto_envelope_from_dict = ReturnRequestDtoEnvelope.from_dict(return_request_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


