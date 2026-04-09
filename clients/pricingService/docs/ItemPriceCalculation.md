# ItemPriceCalculation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** |  | [optional] 
**item_id** | **str** |  | [optional] 
**item** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**price_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**discount_id** | **str** |  | [optional] 
**discount_list_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**rounding_policy_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**effective_discount_percent** | **float** |  | [optional] [readonly] 
**effective_tax_percent** | **float** |  | [optional] [readonly] 
**currency_id** | **str** |  | [optional] 
**currency** | [**CurrencyId**](CurrencyId.md) |  | [optional] 
**total_base_amount** | [**Money**](Money.md) |  | [optional] 
**total_profit_amount** | [**Money**](Money.md) |  | [optional] 
**total_detail_amount** | [**Money**](Money.md) |  | [optional] 
**total_discounts_amount** | [**Money**](Money.md) |  | [optional] 
**total_surcharges_amount** | [**Money**](Money.md) |  | [optional] 
**total_tax_base_amount** | [**Money**](Money.md) |  | [optional] 
**total_tax_amount** | [**Money**](Money.md) |  | [optional] 
**total_w_tax_amount** | [**Money**](Money.md) |  | [optional] 
**total_shipping_cost_amount** | [**Money**](Money.md) |  | [optional] 
**total_shipping_tax_amount** | [**Money**](Money.md) |  | [optional] 
**total_amount** | [**Money**](Money.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_price_calculation import ItemPriceCalculation

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPriceCalculation from a JSON string
item_price_calculation_instance = ItemPriceCalculation.from_json(json)
# print the JSON string representation of the object
print(ItemPriceCalculation.to_json())

# convert the object into a dict
item_price_calculation_dict = item_price_calculation_instance.to_dict()
# create an instance of ItemPriceCalculation from a dict
item_price_calculation_from_dict = ItemPriceCalculation.from_dict(item_price_calculation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


