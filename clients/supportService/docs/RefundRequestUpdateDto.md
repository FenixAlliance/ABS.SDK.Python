# RefundRequestUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 
**approved_timestamp** | **datetime** |  | [optional] 
**support_entitlement_id** | **str** |  | [optional] 
**refund_policy_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.refund_request_update_dto import RefundRequestUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of RefundRequestUpdateDto from a JSON string
refund_request_update_dto_instance = RefundRequestUpdateDto.from_json(json)
# print the JSON string representation of the object
print(RefundRequestUpdateDto.to_json())

# convert the object into a dict
refund_request_update_dto_dict = refund_request_update_dto_instance.to_dict()
# create an instance of RefundRequestUpdateDto from a dict
refund_request_update_dto_from_dict = RefundRequestUpdateDto.from_dict(refund_request_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


