# OrderCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**closed** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**payment_term_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
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
**total_shipping_cost** | **float** |  | [optional] 
**total_shipping_cost_currency_id** | **str** |  | [optional] 
**total_shipping_tax** | **float** |  | [optional] 
**total_shipping_tax_currency_id** | **str** |  | [optional] 
**total_withheld_tax** | **float** |  | [optional] 
**total_withheld_tax_currency_id** | **str** |  | [optional] 
**total_tax_base** | **float** |  | [optional] 
**total_tax_base_currency_id** | **str** |  | [optional] 
**total_taxes** | **float** |  | [optional] 
**total_taxes_currency_id** | **str** |  | [optional] 
**total_global_surcharges** | **float** |  | [optional] 
**total_global_surcharges_currency_id** | **str** |  | [optional] 
**total_global_discounts** | **float** |  | [optional] 
**total_global_discounts_currency_id** | **str** |  | [optional] 
**total** | **float** |  | [optional] 
**total_currency_id** | **str** |  | [optional] 
**cost_calculation_method** | **str** |  | [optional] 
**tax_calculation_method** | **str** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**parent_order_id** | **str** |  | [optional] 
**shipping_method_id** | **str** |  | [optional] 
**billing_location_id** | **str** |  | [optional] 
**customer_notes** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 
**quote_status** | **str** |  | [optional] 
**freight_terms** | **str** |  | [optional] 
**receiver_tenant_id** | **str** |  | [optional] 
**shipping_location_id** | **str** |  | [optional] 
**qualified_identifier** | **str** |  | [optional] 
**total_taxes_in_usd** | **float** |  | [optional] 
**total_discounts_in_usd** | **float** |  | [optional] 
**total_surcharges_in_usd** | **float** |  | [optional] 
**total_shipping_cost_in_usd** | **float** |  | [optional] 
**total_shipping_tax_in_usd** | **float** |  | [optional] 
**total_amount_in_usd** | **float** |  | [optional] 
**effective_to** | **datetime** |  | [optional] 
**effective_from** | **datetime** |  | [optional] 
**order_lines** | [**List[OrderLineCreateDto]**](OrderLineCreateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.order_create_dto import OrderCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateDto from a JSON string
order_create_dto_instance = OrderCreateDto.from_json(json)
# print the JSON string representation of the object
print(OrderCreateDto.to_json())

# convert the object into a dict
order_create_dto_dict = order_create_dto_instance.to_dict()
# create an instance of OrderCreateDto from a dict
order_create_dto_from_dict = OrderCreateDto.from_dict(order_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


