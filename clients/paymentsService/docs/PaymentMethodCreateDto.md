# PaymentMethodCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_create_dto import PaymentMethodCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCreateDto from a JSON string
payment_method_create_dto_instance = PaymentMethodCreateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCreateDto.to_json())

# convert the object into a dict
payment_method_create_dto_dict = payment_method_create_dto_instance.to_dict()
# create an instance of PaymentMethodCreateDto from a dict
payment_method_create_dto_from_dict = PaymentMethodCreateDto.from_dict(payment_method_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


