# RefundRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**approved_timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 
**refund_policy_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.refund_request_dto import RefundRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RefundRequestDto from a JSON string
refund_request_dto_instance = RefundRequestDto.from_json(json)
# print the JSON string representation of the object
print(RefundRequestDto.to_json())

# convert the object into a dict
refund_request_dto_dict = refund_request_dto_instance.to_dict()
# create an instance of RefundRequestDto from a dict
refund_request_dto_from_dict = RefundRequestDto.from_dict(refund_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


