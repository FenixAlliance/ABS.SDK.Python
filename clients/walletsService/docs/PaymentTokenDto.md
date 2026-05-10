# PaymentTokenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**test** | **bool** |  | [optional] 
**mask** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**card_franchise** | **str** |  | [optional] 
**card_expiration_month** | **str** |  | [optional] 
**card_expiration_year** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**valid_until** | **datetime** |  | [optional] 
**wallet_account_id** | **str** |  | [optional] 
**payment_gateway_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_token_dto import PaymentTokenDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTokenDto from a JSON string
payment_token_dto_instance = PaymentTokenDto.from_json(json)
# print the JSON string representation of the object
print(PaymentTokenDto.to_json())

# convert the object into a dict
payment_token_dto_dict = payment_token_dto_instance.to_dict()
# create an instance of PaymentTokenDto from a dict
payment_token_dto_from_dict = PaymentTokenDto.from_dict(payment_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


