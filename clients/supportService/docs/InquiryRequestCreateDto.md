# InquiryRequestCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | 
**organization_name** | **str** |  | [optional] 
**job_role** | **str** |  | [optional] 
**organization_domain** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**message** | **str** |  | 
**social_profile_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inquiry_request_create_dto import InquiryRequestCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InquiryRequestCreateDto from a JSON string
inquiry_request_create_dto_instance = InquiryRequestCreateDto.from_json(json)
# print the JSON string representation of the object
print(InquiryRequestCreateDto.to_json())

# convert the object into a dict
inquiry_request_create_dto_dict = inquiry_request_create_dto_instance.to_dict()
# create an instance of InquiryRequestCreateDto from a dict
inquiry_request_create_dto_from_dict = InquiryRequestCreateDto.from_dict(inquiry_request_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


