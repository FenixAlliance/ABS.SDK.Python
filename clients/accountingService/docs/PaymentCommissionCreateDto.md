# PaymentCommissionCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**payment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_commission_create_dto import PaymentCommissionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCommissionCreateDto from a JSON string
payment_commission_create_dto_instance = PaymentCommissionCreateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentCommissionCreateDto.to_json())

# convert the object into a dict
payment_commission_create_dto_dict = payment_commission_create_dto_instance.to_dict()
# create an instance of PaymentCommissionCreateDto from a dict
payment_commission_create_dto_from_dict = PaymentCommissionCreateDto.from_dict(payment_commission_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


