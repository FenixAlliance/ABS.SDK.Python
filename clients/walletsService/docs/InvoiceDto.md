# InvoiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**closed** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**receiver_tenant_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**customer_notes** | **str** |  | [optional] 
**tax_calculation_method** | **str** |  | [optional] 
**cost_calculation_method** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**total_detail** | **float** |  | [optional] 
**total_detail_currency_id** | **str** |  | [optional] 
**total_profit** | **float** |  | [optional] 
**total_profit_currency_id** | **str** |  | [optional] 
**total_discounts** | **float** |  | [optional] 
**total_discounts_currency_id** | **str** |  | [optional] 
**total_surcharges** | **float** |  | [optional] 
**total_surcharges_currency_id** | **str** |  | [optional] 
**total_tax_base** | **float** |  | [optional] 
**total_tax_base_currency_id** | **str** |  | [optional] 
**total_taxes** | **float** |  | [optional] 
**total_taxes_currency_id** | **str** |  | [optional] 
**total_shipping_cost** | **float** |  | [optional] 
**total_shipping_cost_currency_id** | **str** |  | [optional] 
**total_shipping_tax** | **float** |  | [optional] 
**total_shipping_tax_currency_id** | **str** |  | [optional] 
**total_withheld_tax** | **float** |  | [optional] 
**total_withheld_tax_currency_id** | **str** |  | [optional] 
**total_global_discounts** | **float** |  | [optional] 
**total_global_discounts_currency_id** | **str** |  | [optional] 
**total_global_surcharges** | **float** |  | [optional] 
**total_global_surcharges_currency_id** | **str** |  | [optional] 
**total** | **float** |  | [optional] 
**total_currency_id** | **str** |  | [optional] 
**total_detail_in_usd** | **float** |  | [optional] 
**total_profit_in_usd** | **float** |  | [optional] 
**total_discounts_in_usd** | **float** |  | [optional] 
**total_surcharges_in_usd** | **float** |  | [optional] 
**total_tax_base_in_usd** | **float** |  | [optional] 
**total_taxes_in_usd** | **float** |  | [optional] 
**total_withheld_taxes_in_usd** | **float** |  | [optional] 
**total_shipping_cost_in_usd** | **float** |  | [optional] 
**total_shipping_taxes_in_usd** | **float** |  | [optional] 
**total_global_discounts_in_usd** | **float** |  | [optional] 
**total_global_surcharges_in_usd** | **float** |  | [optional] 
**total_in_usd** | **float** |  | [optional] 
**paid** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**enumeration** | **str** |  | [optional] 
**payment_mode_id** | **str** |  | [optional] 
**enumeration_range_id** | **str** |  | [optional] 
**emisor_billing_profile_id** | **str** |  | [optional] 
**receiver_billing_profile_id** | **str** |  | [optional] 
**emisor_wallet_account_id** | **str** |  | [optional] 
**receiver_wallet_account_id** | **str** |  | [optional] 
**payment_due** | **datetime** |  | [optional] 
**invoice_type** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**invoice_status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_dto import InvoiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDto from a JSON string
invoice_dto_instance = InvoiceDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceDto.to_json())

# convert the object into a dict
invoice_dto_dict = invoice_dto_instance.to_dict()
# create an instance of InvoiceDto from a dict
invoice_dto_from_dict = InvoiceDto.from_dict(invoice_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


