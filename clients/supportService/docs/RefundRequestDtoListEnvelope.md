# RefundRequestDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[RefundRequestDto]**](RefundRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.refund_request_dto_list_envelope import RefundRequestDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of RefundRequestDtoListEnvelope from a JSON string
refund_request_dto_list_envelope_instance = RefundRequestDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(RefundRequestDtoListEnvelope.to_json())

# convert the object into a dict
refund_request_dto_list_envelope_dict = refund_request_dto_list_envelope_instance.to_dict()
# create an instance of RefundRequestDtoListEnvelope from a dict
refund_request_dto_list_envelope_from_dict = RefundRequestDtoListEnvelope.from_dict(refund_request_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


