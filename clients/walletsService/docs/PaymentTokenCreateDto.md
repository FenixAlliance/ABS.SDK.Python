# PaymentTokenCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**mask** | **str** |  | 
**token_type** | **str** |  | [optional] 
**card_franchise** | **str** |  | [optional] 
**card_expiration_month** | **str** |  | 
**card_expiration_year** | **str** |  | 
**valid_until** | **datetime** |  | [optional] 
**payment_gateway_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_token_create_dto import PaymentTokenCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTokenCreateDto from a JSON string
payment_token_create_dto_instance = PaymentTokenCreateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentTokenCreateDto.to_json())

# convert the object into a dict
payment_token_create_dto_dict = payment_token_create_dto_instance.to_dict()
# create an instance of PaymentTokenCreateDto from a dict
payment_token_create_dto_from_dict = PaymentTokenCreateDto.from_dict(payment_token_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


