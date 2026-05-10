# InquiryRequestUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**job_role** | **str** |  | [optional] 
**organization_domain** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inquiry_request_update_dto import InquiryRequestUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InquiryRequestUpdateDto from a JSON string
inquiry_request_update_dto_instance = InquiryRequestUpdateDto.from_json(json)
# print the JSON string representation of the object
print(InquiryRequestUpdateDto.to_json())

# convert the object into a dict
inquiry_request_update_dto_dict = inquiry_request_update_dto_instance.to_dict()
# create an instance of InquiryRequestUpdateDto from a dict
inquiry_request_update_dto_from_dict = InquiryRequestUpdateDto.from_dict(inquiry_request_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


