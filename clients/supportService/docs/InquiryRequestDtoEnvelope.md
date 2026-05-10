# InquiryRequestDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**InquiryRequestDto**](InquiryRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.inquiry_request_dto_envelope import InquiryRequestDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InquiryRequestDtoEnvelope from a JSON string
inquiry_request_dto_envelope_instance = InquiryRequestDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(InquiryRequestDtoEnvelope.to_json())

# convert the object into a dict
inquiry_request_dto_envelope_dict = inquiry_request_dto_envelope_instance.to_dict()
# create an instance of InquiryRequestDtoEnvelope from a dict
inquiry_request_dto_envelope_from_dict = InquiryRequestDtoEnvelope.from_dict(inquiry_request_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


