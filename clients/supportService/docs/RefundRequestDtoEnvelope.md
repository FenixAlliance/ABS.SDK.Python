# RefundRequestDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**RefundRequestDto**](RefundRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.refund_request_dto_envelope import RefundRequestDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of RefundRequestDtoEnvelope from a JSON string
refund_request_dto_envelope_instance = RefundRequestDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(RefundRequestDtoEnvelope.to_json())

# convert the object into a dict
refund_request_dto_envelope_dict = refund_request_dto_envelope_instance.to_dict()
# create an instance of RefundRequestDtoEnvelope from a dict
refund_request_dto_envelope_from_dict = RefundRequestDtoEnvelope.from_dict(refund_request_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


