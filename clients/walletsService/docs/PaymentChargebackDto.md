# PaymentChargebackDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**request_date** | **datetime** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**bank_profile_id** | **str** |  | [optional] 
**bank_profile_name** | **str** |  | [optional] 
**total_fees** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.payment_chargeback_dto import PaymentChargebackDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentChargebackDto from a JSON string
payment_chargeback_dto_instance = PaymentChargebackDto.from_json(json)
# print the JSON string representation of the object
print(PaymentChargebackDto.to_json())

# convert the object into a dict
payment_chargeback_dto_dict = payment_chargeback_dto_instance.to_dict()
# create an instance of PaymentChargebackDto from a dict
payment_chargeback_dto_from_dict = PaymentChargebackDto.from_dict(payment_chargeback_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


