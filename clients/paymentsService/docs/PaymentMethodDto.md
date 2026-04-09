# PaymentMethodDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_method_dto import PaymentMethodDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodDto from a JSON string
payment_method_dto_instance = PaymentMethodDto.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodDto.to_json())

# convert the object into a dict
payment_method_dto_dict = payment_method_dto_instance.to_dict()
# create an instance of PaymentMethodDto from a dict
payment_method_dto_from_dict = PaymentMethodDto.from_dict(payment_method_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


