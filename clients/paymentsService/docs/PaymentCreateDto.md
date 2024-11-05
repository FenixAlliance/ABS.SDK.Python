# PaymentCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**invoice_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**emisor_wallet_id** | **str** |  | [optional] 
**receiver_wallet_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**total_cost** | **float** |  | [optional] 
**total_taxes** | **float** |  | [optional] 
**closed** | **bool** |  | [optional] 
**data** | **str** |  | [optional] 
**data_label** | **str** |  | [optional] 
**data1** | **str** |  | [optional] 
**data1_label** | **str** |  | [optional] 
**response** | **str** |  | [optional] 
**authorization** | **str** |  | [optional] 
**reference_code** | **str** |  | [optional] 
**correlation_code** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**on_behalf_of** | **int** |  | [optional] 
**payment_type** | **int** |  | [optional] 
**payment_status** | **int** |  | [optional] 
**base_cost** | **float** |  | [optional] 
**signature** | **str** |  | [optional] 
**signature_mismatch** | **bool** |  | [optional] 
**is_external** | **bool** |  | [optional] 
**marked_for_revision** | **bool** |  | [optional] 
**forex_rates_snapshot** | **str** |  | [optional] 
**official_id** | **str** |  | [optional] 
**official_id_expedition_date** | **datetime** |  | [optional] 
**fiscal_identification_type_id** | **str** |  | [optional] 
**billing_address** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**cellphone** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**anti_fraud_score** | **float** |  | [optional] 
**call_record_url** | **str** |  | [optional] 
**called** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**payer_picture_timestamp** | **str** |  | [optional] 
**payer_picture** | **str** |  | [optional] 
**identification_picture_timestamp** | **str** |  | [optional] 
**identification_picture** | **str** |  | [optional] 
**identification_back_picture** | **str** |  | [optional] 
**identification_back_picture_timestamp** | **str** |  | [optional] 
**ip_lookup_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**accounting_entry_id** | **str** |  | [optional] 
**payment_gateway_id** | **str** |  | [optional] 
**bank_account_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**bank_id** | **str** |  | [optional] 
**payment_token_id** | **str** |  | [optional] 
**emisor_wallet_account_id** | **str** |  | [optional] 
**receiver_wallet_account_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_create_dto import PaymentCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCreateDto from a JSON string
payment_create_dto_instance = PaymentCreateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentCreateDto.to_json())

# convert the object into a dict
payment_create_dto_dict = payment_create_dto_instance.to_dict()
# create an instance of PaymentCreateDto from a dict
payment_create_dto_from_dict = PaymentCreateDto.from_dict(payment_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


