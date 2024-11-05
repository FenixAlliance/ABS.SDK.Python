# QuoteLineUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed** | **bool** |  | [optional] 
**item_id** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**item_short_description** | **str** |  | [optional] 
**item_primary_image_url** | **str** |  | [optional] 
**shipping_policy_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**free** | **bool** |  | [optional] 
**free_reason** | **str** |  | [optional] 
**free_reason_code** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**data_label** | **str** |  | [optional] 
**data1** | **str** |  | [optional] 
**data1_label** | **str** |  | [optional] 
**data2** | **str** |  | [optional] 
**data2_label** | **str** |  | [optional] 
**data3** | **str** |  | [optional] 
**data3_label** | **str** |  | [optional] 
**data4** | **str** |  | [optional] 
**data4_label** | **str** |  | [optional] 
**data5** | **str** |  | [optional] 
**data5_label** | **str** |  | [optional] 
**data6** | **str** |  | [optional] 
**data6_label** | **str** |  | [optional] 
**data7** | **str** |  | [optional] 
**data7_label** | **str** |  | [optional] 
**data8** | **str** |  | [optional] 
**data8_label** | **str** |  | [optional] 
**data9** | **str** |  | [optional] 
**data9_label** | **str** |  | [optional] 
**item_price_id** | **str** |  | [optional] 
**price_list_item_id** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**tax_calculation_method** | **int** |  | [optional] 
**cost_calculation_method** | **int** |  | [optional] 
**forex_rates_snapshot** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**total_base_amount_in_usd** | **float** |  | [optional] 
**total_profit_in_usd** | **float** |  | [optional] 
**total_detail_amount_in_usd** | **float** |  | [optional] 
**total_tax_base_in_usd** | **float** |  | [optional] 
**total_discounts_in_usd** | **float** |  | [optional] 
**total_taxes_in_usd** | **float** |  | [optional] 
**total_withholding_taxes_in_usd** | **float** |  | [optional] 
**total_shipping_cost_in_usd** | **float** |  | [optional] 
**total_shipping_taxes_in_usd** | **float** |  | [optional] 
**total_warranty_cost_in_usd** | **float** |  | [optional] 
**total_return_cost_in_usd** | **float** |  | [optional] 
**total_refund_cost_in_usd** | **float** |  | [optional] 
**total_surcharges_in_usd** | **float** |  | [optional] 
**total_amount_in_usd** | **float** |  | [optional] 
**total_global_discounts_in_usd** | **float** |  | [optional] 
**total_global_surcharges_in_usd** | **float** |  | [optional] 
**custom_global_surcharges_amount** | **float** |  | [optional] 
**custom_global_discounts_amount** | **float** |  | [optional] 
**custom_base_amount** | **float** |  | [optional] 
**custom_detail_amount** | **float** |  | [optional] 
**custom_discounts_amount** | **float** |  | [optional] 
**custom_tax_base** | **float** |  | [optional] 
**custom_surcharges_amount** | **float** |  | [optional] 
**custom_profit_amount** | **float** |  | [optional] 
**custom_shipping_cost_amount** | **float** |  | [optional] 
**custom_shipping_tax_amount** | **float** |  | [optional] 
**custom_tax_amount** | **float** |  | [optional] 
**custom_withholding_tax_amount** | **float** |  | [optional] 
**custom_total_amount** | **float** |  | [optional] 
**return_policy_id** | **str** |  | [optional] 
**refund_policy_id** | **str** |  | [optional] 
**warranty_policy_id** | **str** |  | [optional] 
**shipment_policy_id** | **str** |  | [optional] 
**shipping_location_id** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**quote_item_record_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**parent_billing_item_record_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.quote_line_update_dto import QuoteLineUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLineUpdateDto from a JSON string
quote_line_update_dto_instance = QuoteLineUpdateDto.from_json(json)
# print the JSON string representation of the object
print(QuoteLineUpdateDto.to_json())

# convert the object into a dict
quote_line_update_dto_dict = quote_line_update_dto_instance.to_dict()
# create an instance of QuoteLineUpdateDto from a dict
quote_line_update_dto_from_dict = QuoteLineUpdateDto.from_dict(quote_line_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


