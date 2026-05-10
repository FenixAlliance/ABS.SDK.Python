# InquiryRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
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
**tenant_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inquiry_request_dto import InquiryRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of InquiryRequestDto from a JSON string
inquiry_request_dto_instance = InquiryRequestDto.from_json(json)
# print the JSON string representation of the object
print(InquiryRequestDto.to_json())

# convert the object into a dict
inquiry_request_dto_dict = inquiry_request_dto_instance.to_dict()
# create an instance of InquiryRequestDto from a dict
inquiry_request_dto_from_dict = InquiryRequestDto.from_dict(inquiry_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


