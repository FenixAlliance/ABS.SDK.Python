# PaymentRefundDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**wallet_account_id** | **str** |  | [optional] 
**refund_request_id** | **str** |  | [optional] 
**total_fees** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.payment_refund_dto import PaymentRefundDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundDto from a JSON string
payment_refund_dto_instance = PaymentRefundDto.from_json(json)
# print the JSON string representation of the object
print(PaymentRefundDto.to_json())

# convert the object into a dict
payment_refund_dto_dict = payment_refund_dto_instance.to_dict()
# create an instance of PaymentRefundDto from a dict
payment_refund_dto_from_dict = PaymentRefundDto.from_dict(payment_refund_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


