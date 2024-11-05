# SupportRequestDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**SupportRequestDto**](SupportRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.support_request_dto_envelope import SupportRequestDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SupportRequestDtoEnvelope from a JSON string
support_request_dto_envelope_instance = SupportRequestDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(SupportRequestDtoEnvelope.to_json())

# convert the object into a dict
support_request_dto_envelope_dict = support_request_dto_envelope_instance.to_dict()
# create an instance of SupportRequestDtoEnvelope from a dict
support_request_dto_envelope_from_dict = SupportRequestDtoEnvelope.from_dict(support_request_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

