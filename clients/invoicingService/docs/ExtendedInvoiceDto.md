# ExtendedInvoiceDto


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
**currency_id** | **str** |  | [optional] 
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
**forex_rate** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**total_taxes** | **float** |  | [optional] 
**total_tax_base** | **float** |  | [optional] 
**total_discounts** | **float** |  | [optional] 
**total_surcharges** | **float** |  | [optional] 
**total_global_discounts** | **float** |  | [optional] 
**total_global_surcharges** | **float** |  | [optional] 
**total_taxes_in_usd** | **float** |  | [optional] 
**total_amount_in_usd** | **float** |  | [optional] 
**total_profit_in_usd** | **float** |  | [optional] 
**total_tax_base_in_usd** | **float** |  | [optional] 
**total_discounts_in_usd** | **float** |  | [optional] 
**total_surcharges_in_usd** | **float** |  | [optional] 
**total_detail_amount_in_usd** | **float** |  | [optional] 
**total_global_discounts_in_usd** | **float** |  | [optional] 
**total_global_surcharges_in_usd** | **float** |  | [optional] 
**total_withholding_taxes_in_usd** | **float** |  | [optional] 
**total_shipping_cost_in_usd** | **float** |  | [optional] 
**total_shipping_taxes_in_usd** | **float** |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**total_in_usd** | [**Money**](Money.md) |  | [optional] 
**total_tax_amount_in_usd** | [**Money**](Money.md) |  | [optional] 
**total_tax_base_amount_in_usd** | [**Money**](Money.md) |  | [optional] 
**total_discounts_amount_in_usd** | [**Money**](Money.md) |  | [optional] 
**total_surcharges_amount_in_usd** | [**Money**](Money.md) |  | [optional] 
**total_global_discounts_amount_in_usd** | [**Money**](Money.md) |  | [optional] 
**total_global_surcharges_amount_in_usd** | [**Money**](Money.md) |  | [optional] 
**total_amount** | [**Money**](Money.md) |  | [optional] 
**total_tax_amount** | [**Money**](Money.md) |  | [optional] 
**total_tax_base_amount** | [**Money**](Money.md) |  | [optional] 
**total_discounts_amount** | [**Money**](Money.md) |  | [optional] 
**total_surcharges_amount** | [**Money**](Money.md) |  | [optional] 
**total_global_discounts_amount** | [**Money**](Money.md) |  | [optional] 
**total_global_surcharges_amount** | [**Money**](Money.md) |  | [optional] 
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
**invoice_type** | **int** |  | [optional] 
**document_type** | **int** |  | [optional] 
**invoice_status** | **int** |  | [optional] 
**tenant** | [**TenantDto**](TenantDto.md) |  | [optional] 
**user** | [**SimpleUserDto**](SimpleUserDto.md) |  | [optional] 
**receiver_tenant** | [**TenantDto**](TenantDto.md) |  | [optional] 
**individual** | [**SimpleContactDto**](SimpleContactDto.md) |  | [optional] 
**organization** | [**SimpleContactDto**](SimpleContactDto.md) |  | [optional] 
**enrollment** | [**SimpleTenantEnrolmentDto**](SimpleTenantEnrolmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_invoice_dto import ExtendedInvoiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedInvoiceDto from a JSON string
extended_invoice_dto_instance = ExtendedInvoiceDto.from_json(json)
# print the JSON string representation of the object
print(ExtendedInvoiceDto.to_json())

# convert the object into a dict
extended_invoice_dto_dict = extended_invoice_dto_instance.to_dict()
# create an instance of ExtendedInvoiceDto from a dict
extended_invoice_dto_from_dict = ExtendedInvoiceDto.from_dict(extended_invoice_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


