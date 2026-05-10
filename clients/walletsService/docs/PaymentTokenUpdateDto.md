# PaymentTokenUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mask** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**card_franchise** | **str** |  | [optional] 
**card_expiration_month** | **str** |  | [optional] 
**card_expiration_year** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 
**payment_gateway_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_token_update_dto import PaymentTokenUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTokenUpdateDto from a JSON string
payment_token_update_dto_instance = PaymentTokenUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentTokenUpdateDto.to_json())

# convert the object into a dict
payment_token_update_dto_dict = payment_token_update_dto_instance.to_dict()
# create an instance of PaymentTokenUpdateDto from a dict
payment_token_update_dto_from_dict = PaymentTokenUpdateDto.from_dict(payment_token_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


