# QuoteDto


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
**cart_id** | **str** |  | [optional] 
**effective_to** | **datetime** |  | [optional] 
**effective_from** | **datetime** |  | [optional] 
**quote_status** | **int** |  | [optional] 
**freight_terms** | **int** |  | [optional] 
**cost_calculation_method** | **int** |  | [optional] 
**custom_discounts_amount** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.quote_dto import QuoteDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDto from a JSON string
quote_dto_instance = QuoteDto.from_json(json)
# print the JSON string representation of the object
print(QuoteDto.to_json())

# convert the object into a dict
quote_dto_dict = quote_dto_instance.to_dict()
# create an instance of QuoteDto from a dict
quote_dto_from_dict = QuoteDto.from_dict(quote_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


