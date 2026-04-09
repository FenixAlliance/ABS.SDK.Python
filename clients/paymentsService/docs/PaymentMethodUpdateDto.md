# PaymentMethodUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_update_dto import PaymentMethodUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodUpdateDto from a JSON string
payment_method_update_dto_instance = PaymentMethodUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodUpdateDto.to_json())

# convert the object into a dict
payment_method_update_dto_dict = payment_method_update_dto_instance.to_dict()
# create an instance of PaymentMethodUpdateDto from a dict
payment_method_update_dto_from_dict = PaymentMethodUpdateDto.from_dict(payment_method_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


