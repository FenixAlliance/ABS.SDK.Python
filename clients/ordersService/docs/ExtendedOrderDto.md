# ExtendedOrderDto


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
**order_lines_count** | **int** |  | [optional] 
**quote_id** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**payment_term_id** | **str** |  | [optional] 
**parent_order_id** | **str** |  | [optional] 
**shipping_method_id** | **str** |  | [optional] 
**billing_location_id** | **str** |  | [optional] 
**shipping_location_id** | **str** |  | [optional] 
**qualified_identifier** | **str** |  | [optional] 
**cost_calculation_method** | **int** |  | [optional] 
**freight_terms** | **int** |  | [optional] 
**order_status** | **int** |  | [optional] 
**requested_delivery_date** | **datetime** |  | [optional] 
**custom_tax_amount** | **float** |  | [optional] 
**custom_total_amount** | **float** |  | [optional] 
**custom_detail_amount** | **float** |  | [optional] 
**custom_profit_amount** | **float** |  | [optional] 
**custom_discounts_amount** | **float** |  | [optional] 
**custom_surcharges_amount** | **float** |  | [optional] 
**custom_shipping_tax_amount** | **float** |  | [optional] 
**custom_shipping_cost_amount** | **float** |  | [optional] 
**custom_withholding_tax_amount** | **float** |  | [optional] 
**user** | [**UserDto**](UserDto.md) |  | [optional] 
**tenant** | [**TenantDto**](TenantDto.md) |  | [optional] 
**individual** | [**ContactDto**](ContactDto.md) |  | [optional] 
**organization** | [**ContactDto**](ContactDto.md) |  | [optional] 
**receiver_tenant** | [**TenantDto**](TenantDto.md) |  | [optional] 
**enrollment** | [**TenantEnrolmentDto**](TenantEnrolmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_order_dto import ExtendedOrderDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedOrderDto from a JSON string
extended_order_dto_instance = ExtendedOrderDto.from_json(json)
# print the JSON string representation of the object
print(ExtendedOrderDto.to_json())

# convert the object into a dict
extended_order_dto_dict = extended_order_dto_instance.to_dict()
# create an instance of ExtendedOrderDto from a dict
extended_order_dto_from_dict = ExtendedOrderDto.from_dict(extended_order_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


