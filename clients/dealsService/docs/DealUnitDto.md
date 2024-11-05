# DealUnitDto


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
**ordered** | **bool** |  | [optional] 
**deal_unit_feed_id** | **str** |  | [optional] 
**deal_unit_flow_id** | **str** |  | [optional] 
**deal_unit_flow_stage_id** | **str** |  | [optional] 
**billing_location_id** | **str** |  | [optional] 
**shipping_location_id** | **str** |  | [optional] 
**partner_created** | **bool** |  | [optional] 
**partner_collaboration** | **bool** |  | [optional] 
**proposed_solution** | **str** |  | [optional] 
**current_situation** | **str** |  | [optional] 
**customer_need** | **str** |  | [optional] 
**won_date** | **datetime** |  | [optional] 
**lost_date** | **datetime** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**delivered_date** | **datetime** |  | [optional] 
**closed_timestamp** | **datetime** |  | [optional] 
**expected_close_date** | **datetime** |  | [optional] 
**deal_unit_status** | **int** |  | [optional] 
**deal_unit_purchase_process** | **int** |  | [optional] 
**deal_unit_forecast_category** | **int** |  | [optional] 
**deal_unit_amounts_calculation** | **int** |  | [optional] 
**lines_count** | **int** |  | [optional] 
**custom_total_amount** | **float** |  | [optional] 
**custom_detail_amount** | **float** |  | [optional] 
**custom_profit_amount** | **float** |  | [optional] 
**custom_shipping_cost_amount** | **float** |  | [optional] 
**custom_withholding_tax_amount** | **float** |  | [optional] 
**custom_surcharges_amount** | **float** |  | [optional] 
**custom_discounts_amount** | **float** |  | [optional] 
**custom_shipping_tax_amount** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.deal_unit_dto import DealUnitDto

# TODO update the JSON string below
json = "{}"
# create an instance of DealUnitDto from a JSON string
deal_unit_dto_instance = DealUnitDto.from_json(json)
# print the JSON string representation of the object
print(DealUnitDto.to_json())

# convert the object into a dict
deal_unit_dto_dict = deal_unit_dto_instance.to_dict()
# create an instance of DealUnitDto from a dict
deal_unit_dto_from_dict = DealUnitDto.from_dict(deal_unit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


