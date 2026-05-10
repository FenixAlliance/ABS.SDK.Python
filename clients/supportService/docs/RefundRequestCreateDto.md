# RefundRequestCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**approved_timestamp** | **datetime** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**refund_policy_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.refund_request_create_dto import RefundRequestCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of RefundRequestCreateDto from a JSON string
refund_request_create_dto_instance = RefundRequestCreateDto.from_json(json)
# print the JSON string representation of the object
print(RefundRequestCreateDto.to_json())

# convert the object into a dict
refund_request_create_dto_dict = refund_request_create_dto_instance.to_dict()
# create an instance of RefundRequestCreateDto from a dict
refund_request_create_dto_from_dict = RefundRequestCreateDto.from_dict(refund_request_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


