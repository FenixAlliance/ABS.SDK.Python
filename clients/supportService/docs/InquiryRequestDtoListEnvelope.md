# InquiryRequestDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[InquiryRequestDto]**](InquiryRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.inquiry_request_dto_list_envelope import InquiryRequestDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InquiryRequestDtoListEnvelope from a JSON string
inquiry_request_dto_list_envelope_instance = InquiryRequestDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(InquiryRequestDtoListEnvelope.to_json())

# convert the object into a dict
inquiry_request_dto_list_envelope_dict = inquiry_request_dto_list_envelope_instance.to_dict()
# create an instance of InquiryRequestDtoListEnvelope from a dict
inquiry_request_dto_list_envelope_from_dict = InquiryRequestDtoListEnvelope.from_dict(inquiry_request_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


